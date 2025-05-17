# 🎬 Movie Recommendation Engine

A content-based recommendation system that suggests similar movies using cosine similarity and NLP techniques. The system analyzes movie features like genres, director, cast, and keywords to provide personalized suggestions.

## 🔍 How It Works
- **Data Processing**: Combines multiple features (genres, director, cast, keywords) into a single text vector
- **Vectorization**: Uses `CountVectorizer` to convert text into a numerical matrix
- **Similarity Scoring**: Computes cosine similarity between movies to find the closest matches
- **Recommendation**: Returns the most similar movies to any given input title

## ⚙️ Technical Implementation
- Built with Python's scikit-learn ecosystem (`pandas`, `numpy`, `sklearn`)
- Implements cosine similarity for measuring movie similarity
- Processes the [Movie Dataset](https://github.com/Darshan-dlr/Movie_recommender-using-ML/blob/main/movie_dataset.csv) containing comprehensive movie metadata

## 🚀 How to Use
1. Clone the repository
2. Install dependencies: `pandas`, `numpy`, `scikit-learn`
3. Run the script and input your favorite movie
4. Get 10 most similar movie recommendations

```python
python movie_recommender.py
```

## 📊 Key Features
- Handles missing data gracefully
- Customizable feature combination
- Efficient similarity scoring
- Easy-to-understand recommendation output

