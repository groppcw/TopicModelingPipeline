source settings.py

cd ${HERE}/partial_results #should dump the logfiles into partial_results

  infile="${HERE}/subcorpora/time-all.dat"
  if ((HOLDOUT_MOD > 0)); then
    infile="${HERE}/subcorpora/time-all-holdout.dat"
  fi

  echo "#!/bin/bash

#PBS -N topic_mix
#PBS -l select=1:mem=4gb
#PBS -l walltime=4:00:00
#PBS -j oe

cd ${HERE}/partial_results

module add gcc

${PLDA_INFER_LOC} \
        --alpha 0.1 \
        --beta 0.01 \
        --inference_data_file ${infile} \
        --inference_result_file $HERE/mixtures/time-all.local \
        --model_file ${HERE}/local_models/time-all.model \
        --total_iterations ${PLDA_INFER_ITERS} \
        --burn_in_iterations ${PLDA_INFER_BURN_IN}" > ${HERE}/partial_results/qinfer.sh
  qsub ${HERE}/partial_results/qinfer.sh
