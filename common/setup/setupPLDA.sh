# this gets called through the experiment run directory, so that's where it'll find everything

source $PWD/settings.py

FS_HOME="/mnt/efsdata"
SCRIPT_DIR="$FS_HOME/TopicModelingPipeline"

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
echo "cd $PWD" >> EXECUTE_ME.sh
echo "$SCRIPT_DIR/method/PLDA/02-buildTopics.sh" >> EXECUTE_ME.sh
echo "$SCRIPT_DIR/method/PLDA/03-uploadTopicOutput.sh" >> EXECUTE_ME.sh
chmod 755 EXECUTE_ME.sh

# modify script to copy output to S3
# just gonna copy the test file for now, but later 
# this will sync the whole results folder.
# Do note I'll need to modify the code to actually copy the stuff
# we want in S3 to the results folder, right now it's scattered throughout the others. Might be worth moving it there instead of copying, and leaving symbolic links behind?
echo "aws s3 cp test.txt s3://cutopicmodeling/test.txt"
