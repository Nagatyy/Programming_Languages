gradesList = [40, 86.5 , 67.8, 55, 43.7, 85]
gradesList.append(96)
gradesList.append(71)

gradesList.sort()

print("Sorted Grades: " + str(gradesList))

failList = []

while(gradesList[0] <= 59):
	failList.append(gradesList[0])
	gradesList.pop(0)

for i in failList:
	print(i)




