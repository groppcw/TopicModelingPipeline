import sys
args = sys.argv

# usage: <source corpus name> <cross validation size>
# for example, "pldaHoldouts /stuff/data/corpus.full.dat 5" to produce 5-fold

if len(args) != 3:
  print "Usage:", args[0], "<full corpus file> <cross validation size>"
  exit(-1)

srcfilename = args[1]
xfold = args[2]

# if the corpus path ends in .full.txt, these will be stripped before the rest of the filenames are tacked on. otherwise, it'll just put everything after the original filename.

# Returns srcfilename if it doesn't end in .full.dat, otherwise just rips that off the end.
srcfileprefix = srcfilename.rsplit(".full.dat",1)[0]

trainFiles = list()
holdoutFiles = list()
for i in range(int(xfold)):
  trainFiles.append(open(srcfileprefix + ".train." + str(i) + "." + str(xfold),"w"))
  holdoutFiles.append(open(srcfileprefix + ".holdout." + str(i) + "." + str(xfold),"w"))

srcfile = open(srcfilename,"r")

for counter, doc in enumerate(srcfile):
  val = counter % int(xfold)
  for holdout in range(int(xfold)):
    if val == holdout:
      holdoutFiles[holdout].write(doc)
    else:
      trainFiles[holdout].write(doc)

srcfile.close()
for trainFile in trainFiles:
  trainFile.close()
for holdoutFile in holdoutFiles:
  holdoutFile.close()
