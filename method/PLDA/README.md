# Run PLDA+ on raw text data, and analyze results.

This directory contains scripts which will run PLDA+ on a given corpus of raw text data. Simply modify the settings file to contain the location where your data is located, and run the scripts in numbered order. These scripts will convert the data into the input format used by PLDA+ and extract other information needed by later scripts, run PLDA+ on the data, and perform post-processing to gather useful information from the run. This includes generating top words for each topic, and calculating perplexity.

Settings file information:
settings.py is designed to be importable by both python and bash scripts, which is why everything is of the form "VARIABLE=VALUE". This file contains information on where the various scripts need to read or place files they interact with, as well as hyperparameters for the methods themselves, such as the topic count, alpha values, and so on. This file also contains information on where various third party software is installed.
* Third party code locations:
** PLDA_LOC - Set this to the filesystem location of the mpi_infer script in your PLDA+ install. For information on how to install PLDA+, please check the readme file in the common/PLDA directory.

Readme last modified May 3rd, 2017.
