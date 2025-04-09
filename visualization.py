import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_rating_distribution(ratings):
    """Plot distribution of ratings"""
    plt.figure(figsize=(10, 6))
    sns.countplot(x='rating', data=ratings)
    plt.title('Distribution of Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.savefig('ratings_distribution.png')
    plt.close()

def plot_model_comparison(metrics_dict):
    """Plot comparison of different recommendation models"""
    models = list(metrics_dict.keys())
    metrics = ['precision', 'recall', 'hit_rate']
    
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    
    for i, metric in enumerate(metrics):
        values = [metrics_dict[model][i] for model in models]
        ax[i].bar(models, values)
        ax[i].set_title(f'{metric.capitalize()}')
        ax[i].set_ylim(0, max(values) * 1.2)
        
    plt.tight_layout()
    plt.savefig('model_comparison.png')
    plt.close()

def plot_user_activity(ratings):
    """Plot user activity distribution"""
    user_counts = ratings.groupby('userId').size().reset_index(name='counts')
    
    plt.figure(figsize=(12, 6))
    sns.histplot(user_counts['counts'], kde=True, bins=30)
    plt.title('Distribution of Ratings per User')
    plt.xlabel('Number of Ratings')
    plt.ylabel('Count of Users')
    plt.savefig('user_activity.png')
    plt.close()
