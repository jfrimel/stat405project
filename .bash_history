ls
cat _condor_stdout
cat _condor_stderr
# After the session starts
tar -xzf python37.tar.gz
export PATH=$PWD/python/bin:$PATH
# Set up Kaggle API credentials
mkdir -p $PWD/.kaggle
cp kaggle.json $PWD/.kaggle/
chmod 600 $PWD/.kaggle/kaggle.json
# Install Kaggle CLI and any other necessary packages
python3 -m pip install --target=$PWD/python/lib/python3.7/site-packages kaggle numpy pandas scikit-learn
/var/lib/condor/execute/slot3/dir_1303799/python/bin/python3 -m pip install --upgrade pip
export PATH=$PWD/python/lib/python3.7/site-packages/bin:$PATH
kaggle --version
# Download the dataset from Kaggle
kaggle datasets download -d gsimonx37/letterboxd -p $PWD --unzip
# Ensure that all necessary CSV files are present
if [ -f actors.csv ] && [ -f countries.csv ] && [ -f crew.csv ] && [ -f genres.csv ] && [ -f languages.csv ] && [ -f movies.csv ] && [ -f releases.csv ] && [ -f studios.csv ] && [ -f themes.csv ]; then     echo "CSV files are present. Proceeding with analysis."     python3 analyze_data.py; else     echo "One or more CSV files are missing. Cannot proceed with analysis.";      python3 analyze_data.py;  q; exit; exit() quit()
clear
ls
    python3 analyze_data.py
clear
    python3 analyze_data.py
clear
    python3 analyze_data.py
ls
cat analyze_data.py 
vim analyze_data.py 
ls
rm analyze_data.py 
vim analyze_data.py
    python3 analyze_data.py
clear
    python3 analyze_data.py
clear
    python3 analyze_data.py
ls
rm analyze_data.py 
vim file.py
ls
    python3 file.py
clear
ls
    python3 file.py
clear
ls
rm file.py 
vim file.py
    python3 file.py
head -n 10 actors.csv
head -n 10 countries.csv
head -n 10 crew.csv
head -n 10 genres.csv
head -n 10 languages.csv
head -n 10 movies.csv
head -n 10 releases.csv
head -n 10 studios.csv
head -n 10 themes.csv
clear
vim file.py
rm file.py 
vim file.py
lcear
clear
ls
python3 file.py 
ls
cat analysis_results.csv 
clear
ls
cat analysis_results.csv 
clear
ls
rm analysis_results.csv 
ls
clear
python3 file.py 
ls
cat analysis_results.csv 
clera
clear
exit 
