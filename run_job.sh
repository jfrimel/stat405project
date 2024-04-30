#!/bin/bash

# Unpack the Python environment
tar -xzf python37.tar.gz
export PATH=$PWD/python/bin:$PATH

# Set up Kaggle API
mkdir -p ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# Install Kaggle CLI (if not already installed)
pip install kaggle --user
export PATH=$HOME/.local/bin:$PATH

# Download the dataset
kaggle datasets download -d gsimonx37/letterboxd
unzip letterboxd.zip -d dataset

# Run your analysis script
python analyze_data.py

# You can specify the output files you want to transfer back in the .sub file
