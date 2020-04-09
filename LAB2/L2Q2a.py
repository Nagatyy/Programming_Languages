bigNum = 1234567
numString = str(bigNum)

print(numString[-3:]) #the last 3 elements

numOfDigits = len(numString)
numOfHyphens =  numOfDigits / 3

myList = []

if numOfDigits % 3 != 0:
	myList.append(numString[0:numOfDigits%3])

for i in range(numOfHyphens):
	myList.append(numString[numOfDigits%3 + (3*i): numOfDigits%3 + (3*i+3)])
	
print(myList)

print("_".join(myList))


