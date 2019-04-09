usernames=['admin','adam','bob','chris','emily']
for user in usernames:
	if user=='admin':
		print("special greetings")
	else:
		print("hello, "+user.title()+" ,welcome logging to the system")	
