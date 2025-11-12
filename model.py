from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import regex as re

app = Flask(__name__)
result=''
# Step 1: Load dataset
df = pd.read_csv('data.csv')

# Step 2: Prepare data
df['text'] = df['City'] + ' ' + df['Category']
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['text'])
df['embedding'] = [vec.toarray()[0] for vec in tfidf_matrix]


# Step 3: Recommendation function
def recommend_places(query, top_n=5):
    query_lower = query.lower()
    filtered_df = df[df['Country'].str.lower() == query_lower]

    # If no match by country, try City
    if filtered_df.empty:
        filtered_df = df[df['City'].str.lower() == query_lower]

    # Empty query
    if query.strip() == "":
        return {
            'message': '',
            'data': []
        }

    # No matches — fallback
    if filtered_df.empty:
        top_global = df.sort_values(by='Rating', ascending=False).head(top_n)
        return {
            'message': f"No results for '{query}'. Showing top-rated global destinations instead.",
            'data': top_global[['Place Name', 'Country', 'Category', 'Rating']].to_dict(orient='records')
        }

    # Compute similarity
    embeddings = np.vstack(filtered_df['embedding'].values)
    similarity_matrix = cosine_similarity(embeddings)
    similarity_scores = similarity_matrix.mean(axis=1)
    filtered_df = filtered_df.copy()
    filtered_df['similarity'] = similarity_scores
    results = filtered_df.sort_values(by='similarity', ascending=False).head(top_n)

    return {
        'message': f"Top {top_n} recommendations for '{query}':",
        'data': results[['Place Name', 'Country', 'City', 'Category']].to_dict(orient='records')
    }


# Step 4: Web Routes
@app.route('/', methods=['GET', 'POST'])
def home():
  #  if request.method == 'POST':
    query = request.form.get('query', '')
    top_n = int(request.form.get('top_n', 5))
    result = recommend_places(query, top_n)
    return render_template('home.html',result=result)


if __name__ == '__main__':
    app.run(debug=True, port=5005)
