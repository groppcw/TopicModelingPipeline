# USAGE: dtm2raw <data-mult.dat> <word_ids.dat> <output.dat>

import sys
if len(argv) != 4:
  print "Usage:",argv[0],"<input data-mult.dat> <input word_ids.dat> <output text file>"
  exit(1)

fdict = open(argv[2],"r")
#fdict = open("./input_data/word_ids.dat","r")
dictionary = dict()
for line in fdict:
     pieces = line.split()
     dictionary[pieces[0]] = (pieces[1].strip()).replace('\"','')

fdict.close()

#wordset = set() # will contain only the words that actually appear in the corpus

fmult = open(argv[1],"r")
ftext = open(argv[3],"w")
for doc in fmult:
  docRHS = (doc.partition(' ')[2]).strip() # rips out uniqueness count and linebreak
  for pair in docRHS.split():
    pieces = pair.split(':')
    word = dictionary[pieces[0]]
    count = pieces[1]
    for unused in range(int(count)):
      ftext.write(word + " ")
#    wordset.add(word)
  ftext.write("\n")
ftext.close()
fmult.close()

#vocab = sorted(list(wordset))
#fvocab = open(argv[4],"w")
#for word in vocab:
#  fvocab.write(word + "\n")
#fvocab.close()
