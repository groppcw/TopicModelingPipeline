from collections import defaultdict

import sys

args = sys.argv

fin = open(args[1],"r")
fout = open(args[2],"w")

fullwc = defaultdict(int)

for line in fin:
    words = line.split()
    wc = defaultdict(int)
    for word in words:
        wc[word] += 1
        fullwc[word] += 1
    for w,c in sorted(wc.iteritems()):
        fout.write(w + " " + str(wc[w]) + " ")
    fout.write("\n")
fin.close()
fout.close()

fdict = open(args[3],"w")
dictkeys = fullwc.keys()
dictkeys.sort()
for word in dictkeys:
  fdict.write(word + "\n")
fdict.close()
