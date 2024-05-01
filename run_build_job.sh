#!/bin/bash

echo "Starting the job..."

# Unpack Python environment
echo "Unpacking Python..."
tar -xzf python37.tar.gz
export PATH=$PWD/python/bin:$PATH
echo "Python unpacked and PATH set."

# Set up Kaggle API credentials
echo "Setting up Kaggle API credentials..."
mkdir -p $PWD/.kaggle
cp kaggle.json $PWD/.kaggle/
chmod 600 $PWD/.kaggle/kaggle.json
echo "Kaggle API credentials set."

# Install necessary Python packages locally
echo "Installing Python packages..."
python3 -m pip install --target=$PWD/python/lib/python3.7/site-packages kaggle numpy pandas scikit-learn
echo "Python packages installed."

# Upgrade pip in the local Python environment
echo "Upgrading pip..."
/var/lib/condor/execute/slot3/dir_1303799/python/bin/python3 -m pip install --upgrade pip
echo "pip upgraded."

# Verify Kaggle CLI installation
echo "Checking Kaggle CLI version..."
kaggle --version
echo "Kaggle CLI version checked."

# Download the dataset from Kaggle
echo "Downloading dataset from Kaggle..."
kaggle datasets download -d gsimonx37/letterboxd -p $PWD --unzip
echo "Dataset downloaded and unzipped."

# Execute the Python analysis script
echo "Running analysis script..."
python3 analyze_data.py
echo "Analysis script completed."

echo "Job completed successfully."
