from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Movie data
movies = {
    "Inception": "Sci-Fi Action",
    "Interstellar": "Sci-Fi Drama",
    "The Dark Knight": "Action Crime",
    "Titanic": "Romance Drama",
    "Avengers": "Action Sci-Fi"
}

movie_names = list(movies.keys())
movie_features = list(movies.values())

# Convert text to vectors
vectorizer = CountVectorizer()
feature_vectors = vectorizer.fit_transform(movie_features)

# Compute similarity
similarity = cosine_similarity(feature_vectors)

# Recommendation function
def recommend(movie):
    index = movie_names.index(movie)
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    print("Recommended movies:")
    for i in scores[1:3]:
        print(movie_names[i[0]])

# Test
recommend("Inception")
