source settings.py

FS_HOME="/mnt/efsdata"

#dir=${EXPERIMENT_DIRECTORY}
#if [ -e $dir ]
#then
#  echo "Experiment directory already exists! Please backup any critical information stored there, delete the directory, and then retry."
#  exit 1
#fi

#mkdir $dir

# build subdirectories

mkdir partial_results
mkdir results
mkdir local_models
mkdir top_words
mkdir mixtures

# copy necessary scripts/build necessary wrappers
echo "$FS_HOME/methods/PLDA/02-buildTopics.sh" > EXECUTE_ME.sh
chmod 755 EXECUTE_ME.sh
