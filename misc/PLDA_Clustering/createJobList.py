# takes an experiment file and tries to replicate what the names of its jobs will be
# basically just expandExperiments.py but without actually performing the expansion

#COPIED FROM EXPAND_EXPERIMENTS:

import sys

# Set some default values. These may be overwritten by the experiment file, but need to exist one way or another.

TOP_X="20" # which sets of top words per topic to generate
HOLDOUT_MOD=0 # x-fold cross validation, if set to 0 doesn't do cross validation at all and just acts on full dataset
METHOD_BURN_IN="50" # for backwards compatibility
USE_SPOTFLEET="false" # determines if this script submits all the jobs or just prepares them for submission
METHOD_ALPHA="false" # if not overwritten, just use the defaults
METHOD_BETA="false" # if not overwritten, just use the defaults

FS_HOME="/mnt/efsdata" # at some point we should be passed this by argument or have it in the file somewhere
EXECUTE_HOME=None # If this gets set, we're splitting execution rather than submitting things as we go.

expFile = sys.argv[1]
execfile(expFile)

itersList = METHOD_ITERS.split()
topicsList = METHOD_TOPICS.split()
alphaList = METHOD_ALPHA.split()
betaList = METHOD_BETA.split()

holdoutList = range(int(HOLDOUT_MOD))
if int(HOLDOUT_MOD) == 0:
  holdoutList = range(1)
  
outfile = open(sys.argv[2],"w")

for rep in range(REPETITIONS):
  for iterationCount in itersList:
    for topicsCount in topicsList:
      for alphaVal in alphaList:
        for betaVal in betaList:
          for holdout in holdoutList:
            # build folder and settings for this specific set of parameters
            repName = "iters-"+str(iterationCount)+"-topics-"+str(topicsCount)
            if alphaVal != "false":
              repName = repName + "-alpha-" + str(alphaVal)
            if betaVal != "false":
              repName = repName + "-beta-" + str(betaVal)
            if int(HOLDOUT_MOD) != 0:
              repName = repName+"-holdout-"+str(holdout)
            repName = repName+"-rep-"+str(rep)
            outfile.write(str(repName) + "\n")
            
outfile.close()
