import sys

topics1 = list()
topics2 = list()

args = sys.argv
if(len(args) != 4):
  print "Usage:",argv[0],"<topics.raw> <topics.raw> <output>"
  exit(1)

f1 = open(args[1],"r")
for line in f1:
  l = list()
  for word in line.split():
    l.append(word.strip())
  topics1.append(set(l))
f1.close()

f2 = open(args[2],"r")
for line in f2:
  l = list()
  for word in line.split():
    l.append(word.strip())
  topics2.append(set(l))
f2.close()

#print(topics1)
#print(topics2)

numiters = min(len(topics1),len(topics2))
outfile = open(args[3],"w")
for unused in range(numiters):
  #find maximum jaccard measure for all matchings
  maxFrom = -1
  maxTo = -1
  maxVal = -1
  dice = -1
  for i in range(0,len(topics1)):
    for j in range(0,len(topics2)):
      jaccard = len(topics1[i].intersection(topics2[j]))/float(len(topics1[i].union(topics2[j])))
      if jaccard > maxVal:
        maxFrom = i
        maxTo = j
        maxVal = jaccard
        dice = 2*len(topics1[i].intersection(topics2[j]))/float(len(topics1[i])+len(topics2[j]))
  outfile.write("Jaccard: " + str(maxVal) + "\n")
  outfile.write("Dice: " + str(dice) + "\n")
  outfile.write(" ".join(topics1[maxFrom]) + "\n")
  outfile.write(" ".join(topics2[maxTo]) + "\n")
  outfile.write("\n")
  topics1.pop(maxFrom)
  topics2.pop(maxTo)

outfile.close()
