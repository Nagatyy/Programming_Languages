
nameList = ["Abdulla mhd zayed", "rashid asif", "john elton rowan smith", "Ali Rami"]
acList = []
finalList = []
for name in nameList:
    w = name.split()
    acList.append((w[0][0],w[-1][0]))

for acronymn in acList:
	finalList.append(''.join(acronymn).upper())

print(finalList)

