source settings.py

cd partial_results

echo "#!/bin/bash

    #PBS -N PLDA_chunk
    #PBS -l select=1:ncpus=${PLDA_CPUS}:mem=16gb:interconnect=mx
    #PBS -l walltime=4:00:00
    #PBS -j oe

    module add gcc
    module add mpich2

    mpiexec -n ${PLDA_CPUS} ${PLDA_LOC} \
        --num_pw ${PLDA_CHUNKS} \
        --num_topics ${LOCAL_TOPICS} \
        --alpha ${PLDA_ALPHA} \
        --beta ${PLDA_BETA} \
        --training_data_file ${HERE}/subcorpora/time-all.dat \
        --model_file ${HERE}/partial_results/time-all-model \
        --total_iterations ${PLDA_ITERS}" > ./qplda.sh
  qsub ./qplda.sh
