file1 = open('email.txt', 'r') 
lines = file1.read()

emailAdds = []
endings = ['com', 'edu', 'gov', 'org']

for string in lines.split():
    if '@' in string:
        emailAdds.append(string)




for email in emailAdds:
	email = email.replace(";","")
	if email[-3:] in endings:
		print(email + " : valid")
	else: 
		print(email + " : INVALID")

	