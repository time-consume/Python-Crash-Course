while True:
	age=input("Indicate your age: ")
	if age=="":
		print("End of this section")
		break
	elif int(age)<3:
		price="free"
	elif int(age)<13:
		price="$10"
	else:
		price="$15"
	print("Your cost is "+price)			
