import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Define paths to files
files = {
    "movies": "movies.csv",
    "actors": "actors.csv",
    "genres": "genres.csv",
    "countries": "countries.csv",
    "crew": "crew.csv",
    "languages": "languages.csv",
    "releases": "releases.csv",
    "studios": "studios.csv",
    "themes": "themes.csv"
}

# Load datasets in chunks and reduce memory usage
def load_data(file_path, usecols=None, chunksize=50000):
    chunks = pd.read_csv(file_path, usecols=usecols, chunksize=chunksize)
    df_list = []
    for chunk in chunks:
        df_list.append(chunk)
    return pd.concat(df_list, ignore_index=True)

# Example usage
try:
    movies = load_data(files['movies'], usecols=['id', 'name', 'date', 'minute', 'rating'])
    genres = load_data(files['genres'], usecols=['id', 'genre'])
except Exception as e:
    print("Error loading data:", e)
    exit()

# Merge datasets
try:
    df = pd.merge(movies, genres, on='id', how='left')
except Exception as e:
    print("Error during merging:", e)
    exit()

# Convert date to datetime and extract year
df['year'] = pd.to_datetime(df['date']).dt.year

# Feature Engineering
df.drop(['date'], axis=1, inplace=True)
df = pd.get_dummies(df, columns=['genre'])

# Clean data: Remove NaN and infinite values before scaling
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# Scale features
scaler = StandardScaler()
df[['minute', 'rating']] = scaler.fit_transform(df[['minute', 'rating']])

# Clustering
kmeans = KMeans(n_clusters=5, random_state=42)
df['cluster'] = kmeans.fit_predict(df[['minute', 'rating']])

# Visualization of clusters
plt.scatter(df['minute'], df['rating'], c=df['cluster'])
plt.title('Cluster of Movies')
plt.xlabel('Normalized Minutes')
plt.ylabel('Normalized Ratings')
plt.colorbar(label='Cluster')
plt.savefig('clusters.png')  # Save the plot as a PNG file
plt.show()

# Regression
X = df.drop(['rating', 'name', 'id'], axis=1)
y = df['rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Print model coefficients mapped to feature names
feature_names = X_train.columns
coef_dict = {feature: coef for feature, coef in zip(feature_names, model.coef_)}
for feature, coef in coef_dict.items():
    print(f"{feature}: {coef}")

# Visualization of feature importance
features = list(coef_dict.keys())
coefficients = list(coef_dict.values())

plt.figure(figsize=(10, 8))
plt.barh(features, coefficients, color='blue')
plt.xlabel('Importance')
plt.ylabel('Features')
plt.title('Feature Importance')
plt.savefig('feature_importance.png')  # Save the plot as a PNG file
plt.show()


df.to_csv('processed_data.csv', index=False)
