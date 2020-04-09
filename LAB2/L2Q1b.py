msg = "Welcome to UAE. uae are awesome, right?"
indexList = []

print("Count: ")
print(msg.upper().count("UAE"))

curr = 0;

while((msg.upper().find("UAE") != -1)):
	indexList.append(msg.upper().find("UAE") + curr)
	curr += msg.upper().find("UAE") + 3
	msg = msg[msg.upper().find("UAE")+3:]


print("Indices of UAE: ")
print(indexList)
