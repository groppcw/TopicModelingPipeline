import sys
import json

dbNameJsonFileLocation = "/opt/CloudyCluster/var/dbName.json"
fileObj = open(str(dbNameJsonFileLocation), "r")
tableObj = json.load(fileObj)
lookupTableName = tableObj['lookupTableName']
objectTableName = tableObj['objectTableName']
tableRegionName = tableObj['tableRegionName']
fileObj.close()

padname = ((str(lookupTableName).split("-"))[1]).strip()

args = sys.argv
execfile(args[1])
settingsFile = open(args[1],"a")
settingsFile.write('S3_PATH="'+str(S3_PATH)+'/'+str(padname)+'"\n')
settingsFile.close()
