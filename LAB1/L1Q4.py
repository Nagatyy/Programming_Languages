values = [50, 12, 27, 33, 61, 49, 28]

for i in range(1, len(values)):
	for j in range(0, len(values)-i):
		if values[j] > values[j+1]:
			values[j], values[j+1] = values[j+1], values[j]


print("Array after bubble sort: " + str(values))
