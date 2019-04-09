active=True
while active:
	age=input("Indicate your age: ")
	if age=="":
		active=False
		print("End of this section")
		continue
	elif int(age)<3:
		price="free"
	elif int(age)<13:
		price="$10"
	else:
		price="$15"
	print("Your cost is "+price)			
