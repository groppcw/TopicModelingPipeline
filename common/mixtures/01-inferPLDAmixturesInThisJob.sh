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


# Go to the partial results to call the inference code, then go back to wherever you were before
current_directory=$PWD
cd ${EXPERIMENT_DIRECTORY}/partial_results #should dump the logfiles into partial_results

  infile="${PLDA_CORPUS_DIRECTORY}/corpus.full.dat"
  if ((HOLDOUT_MOD > 0)); then
    infile="${PLDA_CORPUS_DIRECTORY}/corpus.holdout.${HOLDOUT_IDX}.${HOLDOUT_MOD}"
  fi


#module add gcc

${PLDA_INFER_LOC} \
        --alpha 0.1 \
        --beta 0.01 \
        --inference_data_file ${infile} \
        --inference_result_file ${EXPERIMENT_DIRECTORY}/mixtures/mixtures.dat \
        --model_file ${EXPERIMENT_DIRECTORY}/local_models/full.model \
        --total_iterations ${PLDA_INFER_ITERS} \
        --burn_in_iterations ${PLDA_INFER_BURN_IN}

cd $current_directory
