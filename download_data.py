import pandas as pd
import os
import shutil

try:
    import requests
except ImportError:
    print("Error: 'requests' module not installed.")
    print("Please install required dependencies with:")
    print("pip install -r requirements.txt")
    exit(1)

try:
    import zipfile
    import io
except ImportError:
    print("Error: Required modules not installed.")
    print("Please install required dependencies with:")
    print("pip install -r requirements.txt")
    exit(1)

def download_movielens_dataset():
    # Create data directory
    if not os.path.exists('data'):
        os.makedirs('data')

    # Download MovieLens 100K dataset
    print("Downloading MovieLens dataset...")
    url = 'https://files.grouplens.org/datasets/movielens/ml-latest-small.zip'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses
        
        # Extract files
        z = zipfile.ZipFile(io.BytesIO(response.content))
        z.extractall('data')
        
        # Verify extraction
        expected_files = ['ratings.csv', 'movies.csv']
        extracted_dir = 'data/ml-latest-small'
        
        for file in expected_files:
            if not os.path.exists(os.path.join(extracted_dir, file)):
                print(f"Error: Expected file {file} not found after extraction.")
                return False
                
        print('Dataset downloaded successfully!')
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading dataset: {e}")
        return False
    except zipfile.BadZipFile:
        print("Error: Downloaded file is not a valid zip file.")
        return False

if __name__ == "__main__":
    download_movielens_dataset()
