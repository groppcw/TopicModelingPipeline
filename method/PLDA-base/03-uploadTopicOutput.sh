SETTINGS_DIR=$PWD
DIR=$(dirname $0)

source $SETTINGS_DIR/settings.py

# For each important output, put a link in the results directory.
# Once we have all those set up, copy it out to S3.

# I should probably redirect the error output of all of these to a common error file for the experiment (not this specific run), or do those checks manually.

# Setup links for the topic files.

ln -s $SETTINGS_DIR/local_models/full.model $SETTINGS_DIR/results/full.model
# This can be computed from the full model, so we don't NEED to save it and really don't want to for the huge test.
# ln -s $SETTINGS_DIR/local_models/full.model.normalized $SETTINGS_DIR/results/full.model.normalized

# Setup links for the top words files:
# When top words is changed to be a loop, this code will need to be modified to loop as well.
#ln -s $SETTINGS_DIR/top_words/full-model-top${TOP_X}.txt $SETTINGS_DIR/results/full-model-top${TOP_X}.txt
#ln -s $SETTINGS_DIR/top_words/full-model-top${TOP_X}.raw $SETTINGS_DIR/results/full-model-top${TOP_X}.raw
ln -s $SETTINGS_DIR/top_words/* $SETTINGS_DIR/results/

# Setup links for logging information:
ln -s $SETTINGS_DIR/settings.py $SETTINGS_DIR/results/settings.py
ln -s $SETTINGS_DIR/status.txt $SETTINGS_DIR/results/status.txt
ln -s $SETTINGS_DIR/slurm* $SETTINGS_DIR/results/
ln -s $SETTINGS_DIR/*.log $SETTINGS_DIR/results/

# Send everything to Amazon!
#aws s3 cp $SETTINGS_DIR/results/* s3://cutopicmodeling/temporary_landing_zone/
#aws s3 sync ${SETTINGS_DIR}/results/ ${S3_PATH}/${REP_NAME}/
echo "aws s3 sync ${SETTINGS_DIR}/results/ ${S3_PATH}/${REP_NAME}/"
aws s3 sync ${SETTINGS_DIR}/results/ ${S3_PATH}/${REP_NAME}/
