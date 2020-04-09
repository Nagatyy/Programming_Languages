evenSum, oddSum = 0, 0

for x in range(1,1001):		# 1 ... 1000
	if x%2 is 0: 			# if x is even
		evenSum += x
	else:
		oddSum += x			# if x is odd

print('Even Sum = ' + str(evenSum) + '  Odd Sum= '+ str(oddSum))