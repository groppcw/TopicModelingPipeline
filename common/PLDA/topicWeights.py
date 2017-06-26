#handle settings
import sys
args = sys.argv

if len(args) == 4: # if the user just provided everything we need...
  topicfilename = args[1]
  num_topics = int(args[2])
  outfilename = args[3]
else:
  # we can probably figure all this stuff out from settings variables
  # if they pass us one argument, assume it's a settings location
  # if not, try to load settings where we are and hope for the best
  print "Settings expansion not yet supported for weight calculation. Sorry!"
  exit(1)

# initialize weights at 0 for each topic
weights = list()
for unused in range(num_topics):
  weights.append(0)

topicfile = open(topicfilename,"r")
for word in topicfile: #each line of the topicfile is 1 word x NT topics
  rawvals = word.strip().split() #rips off the linebreak, splits by space
  rawvals = rawvals[1:] #remove leading word, leaving only the values
  for index,val in enumerate(rawvals):
    weights[index] = weights[index] + int(val)

topicfile.close()

total = float(sum(weights))

outfile = open(outfilename,"w")
for index in range(num_topics):
  outfile.write(str(weights[index]) + " ")
outfile.write("\n")
for index in range(num_topics):
  outfile.write(str(float(weights[index])/total) + " ")
outfile.close()
