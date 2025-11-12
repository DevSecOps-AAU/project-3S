# Use an official Python runtime as a base image
FROM python:3.12.3

# Set working directory inside the container
WORKDIR /app

# Copy dependency list and install them
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Flask runs on
EXPOSE 3000
# Command to run the application
CMD ["python", "app.py"]
