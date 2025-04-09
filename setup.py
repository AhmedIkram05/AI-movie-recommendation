from setuptools import setup, find_packages

setup(
    name="movie-recommender",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'scipy',
        'requests',
    ],
    description="Movie recommendation system using collaborative and content-based filtering",
    author="Ahmed Ikram",
)
