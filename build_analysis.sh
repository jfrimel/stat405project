#!/bin/bash
# After the session starts
tar -xzf python37.tar.gz
export PATH=$PWD/python/bin:$PATH

# Set up Kaggle API credentials
mkdir -p $PWD/.kaggle
cp kaggle.json $PWD/.kaggle/
chmod 600 $PWD/.kaggle/kaggle.json

# Install Kaggle CLI and any other necessary packages
python3 -m pip install --target=$PWD/python/lib/python3.7/site-packages kaggle numpy pandas scikit-learn matplotlib seaborn

/var/lib/condor/execute/slot3/dir_1303799/python/bin/python3 -m pip install --upgrade pip

export PATH=$PWD/python/lib/python3.7/site-packages/bin:$PATH
kaggle --version

# Download the dataset from Kaggle
kaggle datasets download -d gsimonx37/letterboxd -p $PWD --unzip

# Extract the dataset files
#unzip letterboxd.zip

python3 analyze_data.py 
python3 analyze_data_2.py

# Clean up downloaded and intermediate files to prevent them from being transferred back
#rm -f *.csv
