# Run PLDA+ on raw text data, and analyze results.

This directory contains scripts which will run PLDA+ on a given corpus of raw text data. Simply modify the settings file to contain the location where your data is located, and run the scripts in numbered order. These scripts will convert the data into the input format used by PLDA+ and extract other information needed by later scripts, run PLDA+ on the data, and perform post-processing to gather useful information from the run. This includes generating top words for each topic, and calculating perplexity.

Settings file information:
settings.py is designed to be importable by both python and bash scripts, which is why everything is of the form "VARIABLE=VALUE". This file contains information on where the various scripts need to read or place files they interact with, as well as hyperparameters for the methods themselves, such as the topic count, alpha values, and so on. This file also contains information on where various third party software is installed.
* Third party code locations:
  * PLDA\_LOC - Set this to the filesystem location of the mpi\_lda script in your PLDA+ install. For information on how to install PLDA+, please check the readme file in the common/PLDA directory. This script is the primary workhorse of PLDA+, and performs topic estimation.
  * PLDA\_INFER\_LOC - Set this to the filesystem location of the infer script in your PLDA+ install. This is the script that performs mixture inference.
* Method Hyperparameters:
  * TOP\_X - How many words to use to represent each topic for topic comparisons and other human readable output files.
  * LOCAL\_TOPICS - How many topics to extract from the data when executing PLDA+.
  * HOLDOUT\_MOD - If performing cross validation, the dataset is divided into this many pieces. To disable cross validation and process the entire dataset as is, set this value to 0.
  * HOLDOUT\_IDX - If using cross validation, this is the index that will be used by executions using this settings file. To get a full set of results, you will need to run the code once with this set to each value between 0 and HOLDOUT\_MOD - 1. (For example, to get a full 5-fold cross validation, run with HOLDOUT\_IDX equal to 0,1,2,3, and 4.)
* Execution parameters:
  * PLDA\_CPUS - The total number of processes being used to execute PLDA+. This is directly input to the mpiexec call.
  * PLDA\_CHUNKS - How many word nodes to use when executing PLDA+. The PLDA+ readme suggests setting this to 1/3 of the total number of cores being used.
  * PLDA\_ITERS - How many iterations to run PLDA+. A low number is unlikely to provide good results, but the exact effects of this parameter have not yet been extensively studied (but it's on the to-do list!).
  * PLDA\_INFER\_ITERS - How many iterations to run PLDA+ mixture inference. As with the previous parameter, high numbers are ostensibly better but the exact effects have not yet been measured.
  * PLDA\_INFER\_BURN\_IN - How many iterations of PLDA+ mixture inference should be considered part of the burn-in period. For a description of what this means, please consult the wikipedia page for Gibbs Sampling. This value must be lower than the total number of iterations.
* File locations:

Readme last modified May 3rd, 2017.
