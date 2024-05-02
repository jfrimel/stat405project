import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
def load_data(filepath):
    return pd.read_csv(filepath)

movies = load_data("movies.csv")
genres = load_data("genres.csv")

# Merge and preprocess data
movies_genres = pd.merge(movies, genres, on='id', how='left')

# Convert date to year and filter recent movies
movies_genres['year'] = pd.to_datetime(movies_genres['date']).dt.year
movies_genres = movies_genres[movies_genres['year'] >= 2010]

# Drop unnecessary columns
movies_genres.drop(['id', 'date', 'tagline', 'description'], axis=1, inplace=True)

# Handle missing values
movies_genres.dropna(subset=['rating', 'minute'], inplace=True)

# Encode genres
movies_genres = pd.get_dummies(movies_genres, columns=['genre'])

# Normalize features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(movies_genres[['minute', 'rating']])
movies_genres[['minute', 'rating']] = scaled_features

# Clustering
kmeans = KMeans(n_clusters=5, random_state=42)
movies_genres['cluster'] = kmeans.fit_predict(movies_genres.drop('name', axis=1))

# Visualization
plt.figure(figsize=(10, 8))
sns.scatterplot(x='minute', y='rating', hue='cluster', data=movies_genres, palette='viridis')
plt.title('Cluster of Movies Based on Normalized Ratings and Duration')
plt.xlabel('Normalized Minutes')
plt.ylabel('Normalized Ratings')
plt.legend(title='Cluster')
plt.savefig('optimized_cluster.png')
plt.show()
