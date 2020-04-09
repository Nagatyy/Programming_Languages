def dictionify(serverInfo):
	db = {}

	for subText in serverInfo:
		subList = subText.split(';')
		listOfDicts = []
		tempDict = {}

		for element in subList:
			if element[0:2] == 'id':
				currID = element.split('=')[1]
				db[currID] = {}
			else:
				tempDict[element.split('=')[0]] = element.split('=')[1]

		db[currID] = tempDict
	return db
################# END OF DICTIONIFY #####################

serverInfo = ("id=0;role=admin;username=joe;surname=naysmith", 
              "surname=suffi;username=sam;role=guest;id=421",
              "id=33;surname=lee;username=mia;role=staff")



db = dictionify(serverInfo)

print(db)

print("################# Query 1 ###############")
for key in db:
	tempDict = db[key]
	print(tempDict['surname'].upper() + ", " + tempDict['username'].upper() \
		+ " - " + tempDict['role'])

print("################# Query 2 ###############")

for key in sorted (db):
	tempDict = db[key]
	print(tempDict['surname'].upper() + ", " + tempDict['username'].upper() \
		+ " - " + tempDict['role'])


