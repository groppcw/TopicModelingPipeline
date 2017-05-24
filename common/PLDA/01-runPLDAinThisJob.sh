# figure out where to find the settings:
if [ -z "$SETTINGS_DIR" ] # if the settings directory isn't already set somewhere earlier...
  then
  if [ $# -eq 0 ] # if no arguments were supplied, guess that it's the PBS directory if that exists, and the working directory if not
    then
    if [ "$PBS_O_WORKDIR" ]
      then
      SETTINGS_DIR=$PBS_O_WORKDIR
    else
      SETTINGS_DIR=$PWD
    fi
  else # if there was an argument provided, just use that
    SETTINGS_DIR=$1
  fi
fi

source $SETTINGS_DIR/settings.py

#module add gcc
#module add mpich2

mpiexec -n ${PLDA_CPUS} ${PLDA_LOC} \
        --num_pw ${PLDA_CHUNKS} \
        --num_topics ${LOCAL_TOPICS} \
        --alpha ${PLDA_ALPHA} \
        --beta ${PLDA_BETA} \
        --training_data_file ${PLDA_CORPUS_DIRECTORY}/corpus.dat \
        --model_file ${EXPERIMENT_DIRECTORY}/partial_results/partial-model \
        --total_iterations ${PLDA_ITERS}
