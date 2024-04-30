import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('letterboxd_data.csv')

# Preprocess the data
df = df.drop(columns=['id', 'title', 'overview', 'tagline', 'poster_path'])  # Drop unnecessary columns
df['release_date'] = pd.to_datetime(df['release_date'])  # Convert release date to datetime
df['year'] = df['release_date'].dt.year  # Extract year from release date

# Perform clustering
kmeans = KMeans(n_clusters=5)
df['cluster'] = kmeans.fit_predict(df[['rating', 'year', 'runtime']])

# Perform regression analysis
X = df[['rating', 'year', 'runtime']]
y = df['cluster']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Save the results to a CSV file
results = pd.DataFrame({'rating': X_test['rating'], 'year': X_test['year'], 'runtime': X_test['runtime'], 'cluster': y_test, 'predicted_cluster': model.predict(X_test)})
results.to_csv('analysis_results.csv', index=False)