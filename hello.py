loop = 'true'	

while(loop == 'true'):
	username = raw_input("Username: ")
	password = raw_input("Password: ")
	if(username == "Snidget" and password == "*Lee"):
		print 'Logged in successfully as ' + username
		loop = 'false'
	else:
		print "Invalid Credentials"

