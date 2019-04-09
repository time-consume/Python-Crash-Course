age=("Pls indicate your age: ")
message=""
while message != 'quit':
	message=input(age)
	if int(message)<3:
		price="free"
	elif int(message)<13:
		price="$10"
	else:
		price="$15"
	print("Your cost is "+price)			
