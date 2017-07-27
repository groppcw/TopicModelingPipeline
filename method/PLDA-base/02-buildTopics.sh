# put job scheduler directives here

SETTINGS_DIR=$PWD
DIR=$(dirname $0)

source $SETTINGS_DIR/settings.py

$DIR/../../common/PLDA/01-runPLDAinThisJob.sh $SETTINGS_DIR
python $DIR/../../common/PLDA/02-collectModel.py $SETTINGS_DIR
python $DIR/../../common/PLDA/03-normalizeModel.py $SETTINGS_DIR
python $DIR/../../common/PLDA/04-topWords.py $SETTINGS_DIR
python $DIR/../../common/PLDA/topicWeights.py $EXPERIMENT_DIRECTORY/local_models/full.model $LOCAL_TOPICS $EXPERIMENT_DIRECTORY/local_models/topic_weights.dat
