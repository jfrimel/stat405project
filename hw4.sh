#!/bin/bash

# Set up environment
tar -xzf R413.tar.gz
tar -xzf packages_FITSio.tar.gz

export PATH=$PWD/R/bin:$PATH
export RHOME=$PWD/R
export R_LIBS=$PWD/packages

# Check and prepare input arguments
DATA_TGZ="$1"  # First argument: the name of the .tgz file containing the data
TEMPLATE_FIT="$2"  # Second argument: the name of the FITS file used as the template

# Unpack the data directory from the provided .tgz file
tar -xzf $DATA_TGZ
DATA_DIR="${DATA_TGZ%.tgz}"  # Removes the .tgz extension to use as the directory name

# Execute the R script with provided template and data directory
Rscript hw4.R $TEMPLATE_FIT $DATA_DIR
