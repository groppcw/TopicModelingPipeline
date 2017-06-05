# take a bunch of model_0 model_1 etc files and merge them alphabetically

# first, import settings;
import sys

print sys.argv

if len(sys.argv) > 1:
  execfile(sys.argv[1] + "/settings.py")
else:
  from settings import *


# for each file, load the file into one giant list
# call sort on the list
# write this output somewhere else

model = dict()

##Add the full vocabulary to the dictionary
##fdict = open("./input_data/word_ids.dat","r")
##for line in fdict:
##  pieces = (line.replace('\t',' ')).split(' ',1)
##  key = (pieces[1].strip()).replace('\"','')
##  value = ''
##  for unused in range(GLOBAL_TOPICS):
##    value = value + '0 '
##  value = value.strip() + '\n'
##  model[key] = value
##fdict.close()

# add dummy values for full vocab, and then replace what we actually have
# this way we make sure the resulting file spans everything in the vocab
# in PLDA, this doesn't matter, but it is critical for certain CLDA scripts
fdict = open(PLDA_CORPUS_DIRECTORY + "/vocab.full.dat","r")
for line in fdict:
  key = line.strip()
  value = ''
  # create empty set of values, will be replaced if it actually appears
  for unused in range(LOCAL_TOPICS): 
    value = value + '0 '
  value = value.strip() + '\n' # remove trailing space
  model[key] = value
fdict.close()

#Replace words that actually appear
for num in range(PLDA_CHUNKS):
  infile = open(EXPERIMENT_DIRECTORY + "/partial_results/partial-model_"+str(num),"r")
  for line in infile:
    # Split the line into the word and the values, so we can do a lookup
    pieces = (line.replace('\t',' ')).split(' ',1)
    # replace the dummy line in the model with the real values
    model[pieces[0]] = pieces[1]
  infile.close()

outmodel = sorted(model) # gives sorted list of keys

outfile = open(EXPERIMENT_DIRECTORY + "/local_models/full.model","w")

for key in outmodel:
  outfile.write(key + " " + model[key])

outfile.close()
