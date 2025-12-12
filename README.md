# Movie Recommendation System

This project implements a movie recommendation system using the MovieLens dataset with collaborative filtering, content-based filtering, and hybrid approaches.

## Project Structure

- `download_data.py`: Downloads the MovieLens dataset
- `data_processing.py`: Data loading and preprocessing functions
- `recommendation_models.py`: Recommendation algorithms implementation
- `evaluation.py`: Metrics for evaluating recommendation quality
- `main.py`: Main script to run the recommendation system
- `visualization.py`: Functions to visualize recommendations and metrics
- `parameter_tuning.py`: Functions to optimize model parameters
- `web_interface.py`: Simple web interface for the recommendation system
- `improve_content_filtering.py`: Enhanced content-based filtering with text analysis

## Setup and Running

1. **Download Models**:
   These files were too big to put in the repo directly so you need to download them from gogle drive then save then in a folder together - 'models' - like i have!

   ```
   https://drive.google.com/drive/folders/1FI-9q4vY10FzzwRcWKqNINUWckav44g5?usp=share_link
   ```

2. **Install dependencies**:

   ```
   pip install -r requirements.txt
   ```

3. **Download the dataset**:

   ```
   python3 download_data.py
   ```

4. **Run the recommendation system**:

   ```
   python3 main.py
   ```

5. **Save trained models for web interface**:

   ```
   python3 save_models.py
   ```

6. **Run the web interface**:

   ```
   python3 web_interface.py
   ```

   Then open <http://localhost:5000> in your browser

## Performance

The current implementation achieves:

- Collaborative Filtering: ~78% hit rate, ~0.22 precision@10
- Hybrid Model: ~74% hit rate, ~0.23 precision@10

## Recommendation Approaches

1. **Collaborative Filtering**: Recommends movies based on user similarity
2. **Content-Based Filtering**: Recommends movies based on content features
3. **Hybrid Approach**: Combines both methods for better recommendations

## Evaluation Metrics

The system uses standard recommendation metrics:

- Precision@k: Proportion of recommended items that are relevant
- Recall@k: Proportion of relevant items that are recommended

## Future Improvements

- Use more advanced matrix factorization techniques
- Incorporate temporal dynamics in user preferences
- Add deep learning models for recommendation
- Implement A/B testing framework
- Deploy as a microservice
