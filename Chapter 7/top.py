prompt="What toppings do you like: \n"
prompt+="Enter quit to end."
while True:
	top=input(prompt)
	if top=='quit':
		break
	print("I'll add "+top+" to your pizza")
	
