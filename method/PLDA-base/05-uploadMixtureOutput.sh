SETTINGS_DIR=$PWD
DIR=$(dirname $0)

source $SETTINGS_DIR/settings.py

# For each important output, put a link in the results directory.
# Once we have all those set up, copy it out to S3.

# I should probably redirect the error output of all of these to a common error file for the experiment (not this specific run), or do those checks manually.

# Setup links for the mixture files.

ln -s $SETTINGS_DIR/mixtures/mixtures.dat $SETTINGS_DIR/results/mixtures.dat
ln -s $SETTINGS_DIR/mixtures/mixtures.normalized.dat $SETTINGS_DIR/results/mixtures.normalized.dat

# Send everything to Amazon!
echo "aws s3 sync ${SETTINGS_DIR}/results/ ${S3_PATH}/${REP_NAME}/"
aws s3 sync ${SETTINGS_DIR}/results/ ${S3_PATH}/${REP_NAME}/
