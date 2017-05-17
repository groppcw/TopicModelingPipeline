# pass in an experiment file, sets up the folders and settings files
import sys
import os
expFile = sys.argv[1]
execfile(expFile)
expName = (expFile.split("."))[0]
expDirname = "EXPERIMENT-"+expName

# mkdir EXPERIMENT-expName
os.system("mkdir -p "+expDirname)
#os.system("cd "+expDirname)
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
      os.system("cp ../../defaultSettings.py settings.py")
      # build rest of specific settings
      settingsFile = open("settings.py","a")
      settingsFile.write('PLDA_LOC="/mnt/efsdata/CU-PLDA-fixed/mpi_lda"\n')
      settingsFile.write('PLDA_INFER_LOC="/mnt/efsdata/CU-PLDA-fixed/infer"\n')
      settingsFile.write('LOCAL_TOPICS='+str(topicsCount)+'\n')
      settingsFile.write('HOLDOUT_MOD=0\n')
      settingsFile.write('TOP_X=20\n')
      totalCores = ARCH_NUM_NODES * ARCH_NUM_CORES
      settingsFile.write('PLDA_CPUS='+str(totalCores)+'\n')
      settingsFile.write('PLDA_CHUNKS='+METHOD_PARTITIONS+'\n')
      settingsFile.write('PLDA_ITERS='+str(iterationCount)+'\n')
      settingsFile.write('RAW_DOC_FILE="/mnt/efsdata/raw_data/'+DATASET_NAME+'/corpus"\n')
      settingsFile.write('PLDA_CORPUS_DIRECTORY="/mnt/efsdata/methods/PLDA/'+DATASET_NAME+'"\n')
      settingsFile.write('EXPERIMENT_DIRECTORY="/mnt/efsdata/methods/PLDA/experiments/'+str(expDirname)+'/'+str(repName)+'"\n')
      settingsFile.close()
      # copy setup script
      #os.system("cp "+INSTALL_SCRIPTS_DIR+"/common/setup/setupPLDA.py .")
      # execute setup script
      #os.system("python setupPLDA.py")

      # go back out of this rep
      os.system("cd ..")
