SETTINGS_DIR=$PWD
DIR=$(dirname $0)

source $SETTINGS_DIR/settings.py

../../common/mixtures/01-inferPLDAmixturesInThisJob.sh
python ../../common/mixtures/02-normalizePLDAmixtures.py $EXPERIMENT_DIRECTORY/mixtures/mixtures.dat $EXPERIMENT_DIRECTORY/mixtures/mixtures.normalized.dat
