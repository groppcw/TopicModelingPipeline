# pass in an experiment file, sets up the folders and settings files
import sys
import os

# Set some default values. These may be overwritten by the experiment file, but need to exist one way or another.

# don't need any here, just leaving the section as boilerplate

# Load the experiment descriptor file.
expFile = sys.argv[1]
execfile(expFile)

FS_HOME="/mnt/efsdata" # at some point we should be passed this by argument or have it in the file somewhere

# get the name of the file, cutting off the directory path and the .py
# this can definitely be cleaned up to allow for differing file organization
expName = (((expFile.split("."))[0]).split("/"))[1]
expDirname = "experiments/"+expName

os.system("mkdir -p "+expDirname)
os.chdir(expDirname)

# define what we do at each descriptor
def callSetup():
  # build folder and settings for this specific set of parameters
  repName = "block-"+str(blockNum)
  os.system("mkdir -p "+str(repName))
  os.chdir(str(repName))

  # copy default settings
  # these are copied for us from the method directory by the parent script
  os.system("pwd")
  os.system("cp ../defaultSettings.py settings.py")
  os.system("cp ../header.sh header.sh")
  os.system("cp header.sh EXECUTE_ME.sh")
  executionFile = open("EXECUTE_ME.sh","a")
  executionFile.write('echo "I did something!" > test.txt\n')
  executionFile.close()
  # build rest of specific settings
  settingsFile = open("settings.py","a")
  settingsFile.write('INPUT_DIRECTORY="'+str(FS_HOME)+'/methods/'+str(METHOD)+'/data/'+str(DATASET_NAME)+'"\n')
  settingsFile.write('EXPERIMENT_DIRECTORY="'+str(FS_HOME)+'/methods/'+str(METHOD)+'/execution/'+str(expDirname)+'/'+str(repName)+'"\n')
  settingsFile.write('REP_NAME="'+str(repName)+'"\n')
  settingsFile.write('S3_PATH="'+str(S3_PATH)+'"\n')
  settingsFile.close()
  # copy over anything specified in the experiment descriptor; most of this will be unused, but it makes it much easier to have users control stuff this way
  os.system("cat "+str(expFile)+" >> settings.py")
  # execute setup script
  os.system(str(FS_HOME)+'/TopicModelingPipeline/method/'+str(METHOD)+'/01-setupExperiment.sh')
  # submit actual job
  os.system(str(SUB_CMD) + " EXECUTE_ME.sh")

  # go back out of this rep into the collective folder
  os.chdir("..")



# loop through descriptor specifications and actually run the above code

blocksList = range(int(METHOD_NUM_BLOCKS))

for blockNum in blocksList:
  callSetup()
