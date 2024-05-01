import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('movies.csv')

# Filter movies by year and minimum duration
df = df[df['date'] >= 2018]
df = df[df['minute'] >= 60]

# Handle missing ratings
df.dropna(subset=['rating'], inplace=True)

# Remove unwanted columns
df.drop(columns=['tagline', 'description'], inplace=True)

# Check and handle 'runtime' if it's referred as 'minute'
if 'runtime' not in df.columns and 'minute' in df.columns:
    df.rename(columns={'minute': 'runtime'}, inplace=True)

# Fill missing runtime values with the mean
df['runtime'] = df['runtime'].fillna(df['runtime'].mean())

# Remove infinite values and fill NaNs
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# Perform clustering
kmeans = KMeans(n_clusters=5)
df['cluster'] = kmeans.fit_predict(df[['rating', 'date', 'runtime']])

# Regression analysis
X = df[['rating', 'date', 'runtime']]
y = df['cluster']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Save the results to a CSV file
results = pd.DataFrame({
    'rating': X_test['rating'],
    'date': X_test['date'],
    'runtime': X_test['runtime'],
    'cluster': y_test,
    'predicted_cluster': model.predict(X_test)
})
results.to_csv('analysis_results.csv', index=False)
