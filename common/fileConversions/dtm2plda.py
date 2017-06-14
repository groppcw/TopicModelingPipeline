# USAGE: dtm2plda <data-mult.dat> <word_ids.dat> <output.dat> <output vocab.dat>

import sys
args = sys.argv
if len(args) != 5:
  print "Usage:",args[0],"<input data-mult.dat> <input word_ids.dat> <output plda data file> <output plda vocab file>"
  exit(1)

fdict = open(args[2],"r")
#fdict = open("./input_data/word_ids.dat","r")
dictionary = dict()
for line in fdict:
     pieces = line.split()
     dictionary[pieces[0]] = (pieces[1].strip()).replace('\"','')

fdict.close()

wordset = set() # will contain only the words that actually appear in the corpus

fmult = open(args[1],"r")
fplda = open(args[3],"w")
for doc in fmult:
  docRHS = (doc.partition(' ')[2]).strip() # rips out uniqueness count and linebreak
  for pair in docRHS.split():
    pieces = pair.split(':')
    word = dictionary[pieces[0]]
    count = pieces[1]
    fplda.write(word + " " + count + " ")
    wordset.add(word)
  fplda.write("\n")
fplda.close()
fmult.close()

vocab = sorted(list(wordset))
fvocab = open(args[4],"w")
for word in vocab:
  fvocab.write(word + "\n")
fvocab.close()
