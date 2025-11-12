from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import regex as re

app = Flask(__name__)

# -----------------------------
# Step 1: Load dataset
# -----------------------------
df = pd.read_csv('data.csv')

# Ensure required columns exist
required_cols = ['Place Name', 'Country', 'City', 'Category', 'Rating']
for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"Missing column in data.csv: {col}")

# -----------------------------
# Step 2: Prepare data (TF-IDF embeddings)
# -----------------------------
df['text'] = df['City'].astype(str) + ' ' + df['Category'].astype(str)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['text'])
df['embedding'] = list(tfidf_matrix.toarray())  # simpler & safer than vec.toarray()[0]

# -----------------------------
# Step 3: Recommendation function
# -----------------------------
def recommend_places(query, top_n=5):
    query = query.strip()
    if query == "":
        return {'message': 'Please enter a valid country or city name.', 'data': []}

    query_lower = query.lower()
    filtered_df = df[df['Country'].str.lower() == query_lower]

    # If no match by country, try City
    if filtered_df.empty:
        filtered_df = df[df['City'].str.lower() == query_lower]

    # Fallback: no matches
    if filtered_df.empty:
        top_global = df.sort_values(by='Rating', ascending=False).head(top_n)
        return {
            'message': f"No results for '{query}'. Showing top-rated global destinations instead.",
            'data': top_global[['Place Name', 'Country', 'Category', 'Rating']].to_dict(orient='records')
        }

    # Compute similarity among places in that city/country
    embeddings = np.vstack(filtered_df['embedding'].values)
    similarity_matrix = cosine_similarity(embeddings)
    similarity_scores = similarity_matrix.mean(axis=1)
    
    filtered_df = filtered_df.copy()
    filtered_df['similarity'] = similarity_scores
    results = filtered_df.sort_values(by='similarity', ascending=False).head(top_n)

    return {
        'message': f"Top {top_n} recommendations for '{query}':",
        'data': results[['Place Name', 'Country', 'City', 'Category', 'similarity']].to_dict(orient='records')
    }

# -----------------------------
# Step 4: Flask route
# -----------------------------
@app.route('/', methods=['GET', 'POST'])
def home():
    result = {'message': '', 'data': []}  # default
    if request.method == 'POST':
        query = request.form.get('query', '')
        top_n = int(request.form.get('top_n', 5))
        result = recommend_places(query, top_n)
    return render_template('home.html', result=result)

# -----------------------------
# Run the app
# -----------------------------
if __name__ == '__main__':
    app.run(debug=False, port=5007)
