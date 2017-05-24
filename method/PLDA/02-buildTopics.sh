# put job scheduler directives here

SETTNGS_DIR=$PWD
DIR=$(dirname $0)

$DIR/../../common/PLDA/01-runPLDAinThisJob.sh $SETTINGS_DIR
python $DIR/../../common/PLDA/02-collectModel.py $SETTINGS_DIR
python $DIR/../../common/PLDA/03-normalizeModel.py $SETTINGS_DIR
