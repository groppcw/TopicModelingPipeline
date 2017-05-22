# this gets called through the experiment run directory, so that's where it'll find everything

source settings.py

FS_HOME="/mnt/efsdata"
SCRIPT_DIR=FS_HOME+"/TopicModelingPipeline"

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
echo "$SCRIPT_DIR/method/PLDA/02-buildTopics.sh" >> EXECUTE_ME.sh
chmod 755 EXECUTE_ME.sh
