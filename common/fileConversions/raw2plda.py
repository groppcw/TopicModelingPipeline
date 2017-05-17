from collections import defaultdict

from settings import *

fin = open(RAW_DOC_FILE + ".txt","r")
fout = open(PLDA_CORPUS_DIRECTORY + "/corpus.full.dat","w")

fullwc = defaultdice(int)

for line in fin:
    words = line.split()
    wc = defaultdict(int)
    for word in words:
        wc[word] += 1
        fullwc[word] += 1
    for w,c in wc.iteritems():
        fout.write(w + " " + str(wc[w]) + " ")
    fout.write("\n")
fin.close()
fout.close()

fdict = open(PLDA_CORPUS_DIRECTORY + "/vocab.full.dat","w")
dictkeys = fullwc.keys()
dictkeys.sort()
for word in dictkeys:
  fdict.write(word + "\n")
fdict.close()
