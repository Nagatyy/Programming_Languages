def phoneFormatter(number, format):
	numbers = []
	c = 0
	for i in format.split("+"):
		numbers.append(number[c: c + int(i)])
		c = c + int(i)
	
	return '-'.join(numbers)

print(phoneFormatter("971506455734","3+2+3+4"))
print(phoneFormatter("33109758351","2+1+2+2+2+2"))
print(phoneFormatter("918966428361","2+3+7"))