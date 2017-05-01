source settings.py

module add gcc
module add mpich2

mpiexec -n ${PLDA_CPUS} ${PLDA_LOC} \
        --num_pw ${PLDA_CHUNKS} \
        --num_topics ${LOCAL_TOPICS} \
        --alpha 0.1 \
        --beta 0.01 \
        --training_data_file ${HERE}/subcorpora/time-all.dat \
        --model_file ${HERE}/partial_results/time-all-model \
        --total_iterations ${PLDA_ITERS}
