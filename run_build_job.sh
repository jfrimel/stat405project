#!/bin/bash

# Unpack the Python environment
tar -xzf python37.tar.gz

# Set up the PATH to include the Python binary
export PATH=$PWD/python/bin:$PATH

# Check if Python is correctly installed
if command -v python >/dev/null 2>&1; then
    echo "Python is available."
else
    echo "Python is not available. Please check the Python installation."
    exit 1
fi

# Set up Kaggle API credentials
mkdir -p ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# Check for pip and install Kaggle CLI
if command -v pip >/dev/null 2>&1; then
    pip install kaggle --user
else
    echo "pip is not available, trying to install it."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py --user
    rm get-pip.py
    export PATH=$HOME/.local/bin:$PATH
    pip install kaggle --user
fi

# Ensure Kaggle CLI is installed
if command -v kaggle >/dev/null 2>&1; then
    echo "Kaggle CLI is ready."
else
    echo "Failed to install Kaggle CLI."
    exit 1
fi

# Download the dataset
kaggle datasets download -d gsimonx37/letterboxd --unzip -p dataset/

# Change to the dataset directory to confirm contents
cd dataset
echo "List of files in the dataset directory:"
ls
