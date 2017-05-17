docsFile = open("time-0.dat","r")
outFile = open("time-0.txt","w")

maxNumWords = 0
for doc in docsFile:
	for enum,element in enumerate(doc.strip().split()):
		if enum % 2 == 0:
			word = element
		else:
			copies = int(element)
			for unused in range(copies):
				outFile.write(word + " ")
	outFile.write("\n")

docsFile.close()
outFile.close()
