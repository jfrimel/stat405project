# Load Python environment
tar -xzf python37.tar.gz
export PATH=$PWD/python/bin:$PATH
# Install Kaggle CLI
pip install kaggle --user
# Configure Kaggle
mkdir -p ~/.kaggle
cp /path/to/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
# Test installation
kaggle datasets list
clear
# Load Python environment
tar -xzf python37.tar.gz
export PATH=$PWD/python/bin:$PATH
exit
