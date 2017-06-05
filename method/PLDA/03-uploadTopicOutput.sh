SETTINGS_DIR=$PWD
DIR=$(dirname $0)

source $SETTINGS_DIR/settings.py

# For each important output, put a link in the results directory.
# Once we have all those set up, copy it out to S3.

# I should probably redirect the error output of all of these to a common error file for the experiment (not this specific run), or do those checks manually.

# Setup links for the topic files.

ln -s $SETTINGS_DIR/local_models/full.model $SETTINGS_DIR/results/full.model
ln -s $SETTINGS_DIR/local_models/full.normalized.model $SETTINGS_DIR/results/full.normalized.model

# Setup links for the top words files:
# When top words is changed to be a loop, this code will need to be modified to loop as well.
ln -s $SETTINGS_DIR/top_words/full-model-top${TOP_X}.txt $SETTINGS_DIR/results/full-model-top${TOP_X}.txt
ln -s $SETTINGS_DIR/top_words/full-model-top${TOP_X}.raw $SETTINGS_DIR/results/full-model-top${TOP_X}.raw

# Send everything to Amazon!
aws s3 cp $SETTINGS_DIR/results/* s3://cutopicmodeling/temporary_landing_zone/
