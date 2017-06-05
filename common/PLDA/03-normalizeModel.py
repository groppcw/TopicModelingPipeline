#take a .model file and normalize each vector to sum to 1

#consider also changing every 0 to a 1 beforehand so that we have a base value for each word to use
#but right now I'm not going to worry about setting an epsilon

# first, import settings;
import sys
if len(sys.argv) > 1:
  execfile(sys.argv[1] + "/settings.py")
else:
  from settings import *

infile = open(EXPERIMENT_DIRECTORY + "/local_models/full.model","r")
outfile = open(EXPERIMENT_DIRECTORY + "/local_models/full.model.normalized","w")

listoflists = []
for line in infile:
  pieces = line.strip().split()
  if len(listoflists) < len(pieces):
    for j in range(len(pieces)):
      listoflists.insert(j,[])
  for pnum,piece in enumerate(pieces):
    listoflists[pnum].append(piece)
  
infile.close()
  
for inum,item in enumerate(listoflists):
  if inum > 0:
    for nnum,num in enumerate(item):
      listoflists[inum][nnum] = float(num)
    s = sum(listoflists[inum])
    for nnum,num in enumerate(item):
      listoflists[inum][nnum] = float(num)/float(s)

for j in range(len(listoflists[0])):
  for k in range(len(listoflists)):
    outfile.write(str(listoflists[k][j])+' ')
  outfile.write('\n')

outfile.close()
