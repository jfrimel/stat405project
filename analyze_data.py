import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('movies.csv')

# Check for the presence of expected columns and drop if they exist
columns_to_drop = ['id', 'name', 'tagline', 'description']
df.drop(columns=[col for col in columns_to_drop if col in df.columns], errors='ignore', inplace=True)

# Convert 'date' to datetime and extract the year if 'date' exists
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year'] = df['date'].dt.year

# Handle potential absence of columns used in clustering and regression
if set(['rating', 'year', 'minute']).issubset(df.columns):
    # Perform clustering
    kmeans = KMeans(n_clusters=5)
    df['cluster'] = kmeans.fit_predict(df[['rating', 'year', 'minute']].dropna())

    # Perform regression analysis
    X = df[['rating', 'year', 'minute']].dropna()
    y = df['cluster']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict and save results
    results = pd.DataFrame({
        'Actual Cluster': y_test,
        'Predicted Cluster': model.predict(X_test),
        'rating': X_test['rating'],
        'year': X_test['year'],
        'minute': X_test['minute']
    })
    results.to_csv('analysis_results.csv', index=False)

    print("Analysis complete. Results saved to 'analysis_results.csv'.")
else:
    print("Error: Required columns for analysis are missing.")

