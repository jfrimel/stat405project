# After the session starts
tar -xzf python37.tar.gz
export PATH=$PWD/python/bin:$PATH

# Install Kaggle CLI and any other necessary packages
python3 -m pip install --target=$PWD/python/lib/python3.7/site-packages kaggle numpy pandas scikit-learn

# Set up Kaggle API credentials
mkdir -p $PWD/.kaggle
cp kaggle.json $PWD/.kaggle/
chmod 600 $PWD/.kaggle/kaggle.json

export PATH=$PWD/python/lib/python3.7/site-packages/bin:$PATH
kaggle --version

# Download the dataset from Kaggle
kaggle datasets download -d gsimonx37/letterboxd -p $PWD --unzip

# Extract the dataset files
unzip letterboxd.zip

# Save the dataset to a CSV file
python3 -c "import pandas as pd; pd.read_csv('letterboxd.csv', header=0).to_csv('letterboxd_data.csv', index=False)"

# Run the Python analysis script
python3 analyze_data.py
