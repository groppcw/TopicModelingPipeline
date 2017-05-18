source settings.py

#module add gcc
#module add mpich2

mpiexec -n ${PLDA_CPUS} ${PLDA_LOC} \
        --num_pw ${PLDA_CHUNKS} \
        --num_topics ${LOCAL_TOPICS} \
        --alpha ${PLDA_ALPHA} \
        --beta ${PLDA_BETA} \
        --training_data_file ${PLDA_CORPUS_DIRECTORY}/time-all.dat \
        --model_file ${EXPERIMENT_DIRECTORY}/partial_results/time-all-model \
        --total_iterations ${PLDA_ITERS}
