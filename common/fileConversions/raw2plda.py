from collections import defaultdict

from settings import *

fin = open(RAW_DOC_FILE,"r")
fout = open(PLDA_DOC_FILE,"w")

for line in fin:
    words = line.split()
    wc = defaultdict(int)
    for word in words:
        wc[word] += 1
    for w,c in wc.iteritems():
        fout.write(w + " " + str(wc[w]) + " ")
    fout.write("\n")
fin.close()
fout.close()

fdict = open(VOCAB_FILE,"w")
dictkeys = wc.keys()
dictkeys.sort()
for word in dictkeys:
  fdict.write(word + "\n")
fdict.close()
