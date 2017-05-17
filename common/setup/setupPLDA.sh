source settings.py

dir=${EXPERIMENT_DIRECTORY}
if [ -e $dir ]
then
  echo "Experiment directory already exists! Please backup any critical information stored there, delete the directory, and then retry."
  exit 1
fi

mkdir $dir

