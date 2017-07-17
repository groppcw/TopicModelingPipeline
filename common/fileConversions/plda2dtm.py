import sys
args = sys.argv

docsfile = open(args[1],"r")
outfile = open(args[2],"w")
vocabfile = open(args[3],"r")

vocab = dict()

for enum,line in enumerate(vocabfile):
  word = line.strip()
  vocab[word] = str(enum)

vocabfile.close()

for doc in docsfile:
  numunique = 0
  thisdoc = ""
  for enum,element in enumerate(doc.strip().split()):
    if enum % 2 == 0:
      word = element
      wordid = vocab[word]
      numunique = numunique + 1
    else:
      copies = element
      thisdoc = thisdoc + " " + wordid + ":" + copies
  outfile.write(str(numunique) + thisdoc + "\n")
docsfile.close()
outfile.close()
