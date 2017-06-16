import sys
args = sys.argv

infile = open(argv[1],"r")
outfile = open(argv[2],"w")

for line in infile:
  entries = line.strip().split()
  linesum = 0
  for entry in entries:
    linesum += float(entry)
  for entry in entries:
    outfile.write(str(float(entry)/linesum)+" ")
  outfile.write("\n")
infile.close()
outfile.close()
