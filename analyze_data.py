import pandas as pd
import sys

def load_data(path):
    return pd.read_csv(path)

def analyze_data(data):
    # Example analysis: Average rating per genre
    return data.groupby('genre')['rating'].mean()

def main(file_path):
    data = load_data(file_path)
    results = analyze_data(data)
    print(results)
    # Save or further process results as needed

if __name__ == "__main__":
    main(sys.argv[1])
