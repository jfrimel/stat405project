#!/bin/bash

# Unpack the Python environment
tar -xzf my_python_env.tar.gz

# Set PATH
export PATH=$PWD/python/bin:$PATH
export KAGGLE_CONFIG_DIR=$PWD

# Download dataset
kaggle datasets download -d gsimonx37/letterboxd -p $PWD --unzip

# Run the analysis script on the downloaded dataset
python analyze_data.py themes.csv
