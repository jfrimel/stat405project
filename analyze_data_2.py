import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

# Paths to files
files = {
    "movies": "movies.csv",
    "actors": "actors.csv",
    "genres": "genres.csv",
    "countries": "countries.csv",
    "languages": "languages.csv",
    "releases": "releases.csv",
    "studios": "studios.csv"
}

# Function to load and concatenate data
def load_data(files):
    data_frames = {}
    for key, filepath in files.items():
        try:
            data_frames[key] = pd.read_csv(filepath)
            print(f"Loaded {key} successfully!")
        except Exception as e:
            print(f"Failed to load {key}: {e}")
    return data_frames

# Load all data
dfs = load_data(files)

# Merge datasets
df = dfs['movies']
df = df.merge(dfs['genres'], on='id', how='left')
df = df.merge(dfs['countries'], on='id', how='left')
df = df.merge(dfs['languages'], on='id', how='left')
df = df.merge(dfs['releases'], on='id', how='left')

# Basic Cleaning
df.dropna(subset=['rating'], inplace=True)
df['year'] = pd.to_datetime(df['date']).dt.year

# One-hot encoding for categorical data
df = pd.get_dummies(df, columns=['genre', 'country', 'language', 'type'])

# Feature scaling
scaler = StandardScaler()
df[['minute', 'rating']] = scaler.fit_transform(df[['minute', 'rating']])

# Linear Regression
X = df.drop(['id', 'name', 'date', 'rating', 'description', 'tagline'], axis=1)
y = df['rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Save linear regression results to a CSV file
results_df = pd.DataFrame({'Actual': y_test, 'Predicted': model.predict(X_test)})
results_df.to_csv('linear_regression_results.csv', index=False)

# Feature Importance Visualization
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
coefficients.sort_values(by='Coefficient', ascending=True, inplace=True)

plt.figure(figsize=(10, 8))
sns.barplot(x=coefficients.Coefficient, y=coefficients.index)
plt.title('Feature Importance in Predicting Movie Ratings')
plt.xlabel('Coefficient')
plt.ylabel('Feature')
plt.savefig('feature_importance_all_factors.png')
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), cmap='coolwarm')
plt.title('Correlation Heatmap of Movie Features')
plt.savefig('correlation_heatmap.png')
plt.show()
