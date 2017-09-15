import sys
import os

args = sys.argv

# 1st arg is S3 path to root experiment
# 2nd arg is file containing list of all desired reps in that experiment
# presumably, to get that 2nd arg, you get the whole list and then grep it, but that's not this script's concern
# 3rd arg is directory to shove all this in

if len(args) != 4:
  print "Usage:",args[0],"<S3 path to experiment> <filename for desired rep list> <directory to place output>"
  exit(-1)

S3path = args[1]
repfilename = args[2]
outputdirectory = args[3]

repfile = open(repfilename,"r")

os.system("mkdir -p " + str(outputdirectory))
os.chdir(str(outputdirectory))

for line in repfile:
  # If you're having problems getting throttled by the AWS API, add a sleep in this loop
  os.system("mkdir -p " + line.strip())
  os.system("aws s3 sync " + str(S3path) + "/" + line.strip() + " " + line.strip())


repfile.close()
