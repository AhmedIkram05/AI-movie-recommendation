import flask
from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import os

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained models
try:
    with open('models/cf_model.pkl', 'rb') as f:
        cf_model = pickle.load(f)
    with open('models/hybrid_model.pkl', 'rb') as f:
        hybrid_model = pickle.load(f)
    movies = pd.read_csv('data/ml-latest-small/movies.csv')
    print("Models and data loaded successfully")
except Exception as e:
    print(f"Error loading models: {e}")
    print("Please run 'python save_models.py' first to train and save models")

@app.route('/')
def index():
    return """
    <h1>Movie Recommendation System</h1>
    <form action="/recommend" method="get">
        <label for="user_id">Enter User ID:</label>
        <input type="number" id="user_id" name="user_id" required>
        <button type="submit">Get Recommendations</button>
    </form>
    """

@app.route('/recommend')
def recommend():
    user_id = int(request.args.get('user_id', 1))
    try:
        # Get recommendations
        cf_recs = cf_model.recommend_items(user_id, n_recommendations=10)
        hybrid_recs = hybrid_model.recommend_items(user_id, n_recommendations=10)
        
        # Add movie details
        if not cf_recs.empty:
            cf_recs = cf_recs.merge(movies[['movieId', 'title']], on='movieId')
        if not hybrid_recs.empty:
            hybrid_recs = hybrid_recs.merge(movies[['movieId', 'title']], on='movieId')
        
        # Generate HTML response
        html = f"<h1>Recommendations for User {user_id}</h1>"
        
        html += "<h2>Collaborative Filtering Recommendations</h2><ul>"
        for _, row in cf_recs.iterrows():
            html += f"<li>{row['title']} (score: {row['score']:.2f})</li>"
        html += "</ul>"
        
        html += "<h2>Hybrid Recommendations</h2><ul>"
        for _, row in hybrid_recs.iterrows():
            html += f"<li>{row['title']} (score: {row['score']:.2f})</li>"
        html += "</ul>"
        
        return html
    except Exception as e:
        return f"Error generating recommendations: {e}"

if __name__ == '__main__':
    # Change port from default 5000 to 8080 to avoid conflicts
    app.run(debug=True, port=8080)
