# pass in an experiment file, sets up the folders and settings files
import sys
import os

# Set some default values. These may be overwritten by the experiment file, but need to exist one way or another.

TOP_X="20" # which sets of top words per topic to generate
HOLDOUT_MOD=0 # x-fold cross validation, if set to 0 doesn't do cross validation at all and just acts on full dataset
METHOD_BURN_IN="50" # for backwards compatibility

FS_HOME="/mnt/efsdata" # at some point we should be passed this by argument or have it in the file somewhere
EXECUTE_HOME=None # If this gets set, we're splitting execution rather than submitting things as we go.

expFile = sys.argv[1]
execfile(expFile)

# get the name of the file, cutting off the directory path and the .py
# this can definitely be cleaned up to allow for differing file organization
expName = (((expFile.split("."))[0]).split("/"))[1]
expDirname = "experiments/"+expName

os.system("mkdir -p "+expDirname)
os.chdir(expDirname)

itersList = METHOD_ITERS.split()
topicsList = METHOD_TOPICS.split()

holdoutList = range(int(HOLDOUT_MOD))
if int(HOLDOUT_MOD) == 0:
  holdoutList = range(1)

for iterationCount in itersList:
  for topicsCount in topicsList:
    for holdout in holdoutList:
      for rep in range(REPETITIONS):
        # build folder and settings for this specific set of parameters
        repName = "iters-"+str(iterationCount)+"-topics-"+str(topicsCount)
        if int(HOLDOUT_MOD) != 0:
          repName = repName+"-holdout-"+str(holdout)
        repName = repName+"-rep-"+str(rep)
        os.system("mkdir -p "+str(repName))
        os.chdir(str(repName))
        #os.system("cd "+repName)

        # copy default settings
        # ostensibly we should have these stored with the actual method
        os.system("pwd")
        os.system("cp ../defaultSettings.py settings.py")
        os.system("cp ../header.sh header.sh")
        os.system("cp header.sh EXECUTE_ME.sh")
        executionFile = open("EXECUTE_ME.sh","a")
        executionFile.write('echo "I did something!" > test.txt\n')
        executionFile.close()
        # build rest of specific settings
        settingsFile = open("settings.py","a")
        settingsFile.write('PLDA_LOC="'+str(FS_HOME)+'/CU-PLDA-fixed/PLDA-base/mpi_lda"\n')
        settingsFile.write('PLDA_INFER_LOC="'+str(FS_HOME)+'/CU-PLDA-fixed/PLDA-base/infer"\n')
        settingsFile.write('LOCAL_TOPICS='+str(topicsCount)+'\n')
        settingsFile.write('HOLDOUT_MOD='+str(HOLDOUT_MOD)+'\n')
        settingsFile.write('HOLDOUT_IDX='+str(holdout)+'\n')
        settingsFile.write('TOP_X='+str(TOP_X)+'\n')
        totalCores = int(METHOD_NUM_NODES) * int(METHOD_NUM_CORES)
        settingsFile.write('PLDA_CPUS='+str(totalCores)+'\n')
        settingsFile.write('PLDA_ITERS='+str(iterationCount)+'\n')
        settingsFile.write('PLDA_BURN_IN='+str(METHOD_BURN_IN)+'\n')
        settingsFile.write('RAW_DOC_FILE="'+str(FS_HOME)+'/raw_data/'+str(DATASET_NAME)+'/corpus"\n')
        settingsFile.write('PLDA_CORPUS_DIRECTORY="'+str(FS_HOME)+'/methods/PLDA-base/data/'+str(DATASET_NAME)+'"\n')
        settingsFile.write('EXPERIMENT_DIRECTORY="'+str(FS_HOME)+'/methods/PLDA-base/execution/'+str(expDirname)+'/'+str(repName)+'"\n')
        settingsFile.write('REP_NAME="'+str(repName)+'"\n')
        settingsFile.write('S3_PATH="'+str(S3_PATH)+'"\n')
        settingsFile.write('FS_HOME="'+str(FS_HOME)+'"\n')
        settingsFile.close()
        ## copy setup script - maybe the script that calls this one should do that? technically we shouldn't necessarily know where this got placed
        #os.system("cp "+FS_HOME+"/TopicModelingPipeline/method/PLDA/01-setupExperiment.sh .")
        #os.system("chmod 755 01-setupExperiment.sh")
        # execute setup script
        #os.system("./01-setupExperiment.sh")
        os.system(str(FS_HOME)+'/TopicModelingPipeline/method/PLDA-base/01-setupExperiment.sh')
        # submit actual job, or set it up for someone else to do it
        if EXECUTE_PATH is not None:
          os.system('echo "cd $PWD ; ' + str(SUB_CMD) + ' EXECUTE_ME.sh" >> ' + str(EXECUTE_PATH))
        else:
          os.system(str(SUB_CMD) + " EXECUTE_ME.sh")

        # go back out of this rep into the collective folder
        os.chdir("..")
