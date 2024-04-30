#!/bin/bash

# Specify paths for Python and R installations on CHTC
PYTHON_DIR="python37.tar.gz"
R_DIR="R405.tar.gz" 

# Download and set up Python and R
echo "Setting up Python and R environments..."
wget http://proxy.chtc.wisc.edu/SQUID/chtc/$PYTHON_DIR
wget http://proxy.chtc.wisc.edu/SQUID/chtc/$R_DIR
tar -xzf $PYTHON_DIR
tar -xzf $R_DIR

# Set environment paths
export PATH=$PWD/python/bin:$PATH
export R_LIBS=$PWD/R/library
export PATH=$PWD/R/bin:$PATH

# Create a directory for data and scripts
mkdir data
mkdir scripts

# Download data
echo "Downloading and unpacking the dataset..."
wget https://www.kaggle.com/datasets/gsimonx37/letterboxd?select=themes.csv -O data/data.zip  # Replace with actual dataset link
unzip data/data.zip -d data

# Move scripts to appropriate location (if they are not already there)
cp /home/jrchristens2/projectCHTC/R_scripts/*.py scripts/
cp /home/jrchristens2/projectCHTC/R_scripts/*.R scripts/

# Navigate to scripts directory
cd scripts

# Run Python analysis
echo "Running Python analysis..."
python3 analyze_data.py

# Run R analysis
echo "Running R analysis..."
Rscript analyze_data.R

# Clean up data and environments
echo "Cleaning up data and environments..."
rm -r $PWD/data
rm -r $PWD/python
rm -r $PWD/R

# Final message
echo "Analysis complete. Clean-up done."
