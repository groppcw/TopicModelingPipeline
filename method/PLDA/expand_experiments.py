# pass in an experiment file, sets up the folders and settings files
import sys
import os
expFile = sys.argv[1]
execfile(expFile)

FS_HOME="/mnt/efsdata" # at some point we should be passed this by argument or have it in the file somewhere

# get the name of the file, cutting off the directory path and the .py
# this can definitely be cleaned up to allow for differing file organization
expName = (((expFile.split("."))[0]).split("/"))[1]
expDirname = "experiments/"+expName

os.system("mkdir -p "+expDirname)
os.chdir(expDirname)

itersList = METHOD_ITERS.split()
topicsList = METHOD_TOPICS.split()

for iterationCount in itersList:
  for topicsCount in topicsList:
    for rep in range(REPETITIONS):
      # build folder and settings for this specific set of parameters
      repName = "iters-"+str(iterationCount)+"-topics-"+str(topicsCount)+"-rep-"+str(rep)
      os.system("mkdir -p "+repName)
      os.chdir(repName)
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
      settingsFile.write('PLDA_LOC="'+FS_HOME+'/CU-PLDA-fixed/mpi_lda"\n')
      settingsFile.write('PLDA_INFER_LOC="'+FS_HOME+'/CU-PLDA-fixed/infer"\n')
      settingsFile.write('LOCAL_TOPICS='+str(topicsCount)+'\n')
      settingsFile.write('HOLDOUT_MOD=0\n')
      settingsFile.write('TOP_X=20\n')
      totalCores = ARCH_NUM_NODES * ARCH_NUM_CORES
      settingsFile.write('PLDA_CPUS='+str(totalCores)+'\n')
      settingsFile.write('PLDA_CHUNKS='+METHOD_PARTITIONS+'\n')
      settingsFile.write('PLDA_ITERS='+str(iterationCount)+'\n')
      settingsFile.write('RAW_DOC_FILE="'+FS_HOME+'/raw_data/'+DATASET_NAME+'/corpus"\n')
      settingsFile.write('PLDA_CORPUS_DIRECTORY="'+FS_HOME+'/methods/PLDA/data/'+DATASET_NAME+'"\n')
      settingsFile.write('EXPERIMENT_DIRECTORY="'+FS_HOME+'/methods/PLDA/execution/'+str(expDirname)+'/'+str(repName)+'"\n')
      settingsFile.close()
      ## copy setup script - maybe the script that calls this one should do that? technically we shouldn't necessarily know where this got placed
      #os.system("cp "+FS_HOME+"/TopicModelingPipeline/method/PLDA/01-setupExperiment.sh .")
      #os.system("chmod 755 01-setupExperiment.sh")
      # execute setup script
      #os.system("./01-setupExperiment.sh")
      os.system(FS_HOME+'/TopicModelingPipeline/method/PLDA/01-setupExperiment.sh')
      # submit actual job
      os.system(SUB_CMD + " EXECUTE_ME.sh")

      # go back out of this rep into the collective folder
      os.chdir("..")
