while(True):
	n1=input("pls enter number 1: ")
	n2=input("pls enter number 2: ")
	try:
		n3=(int(n1)+int(n2))
	except ValueError:
		print("you're not entering a number")
	else:
		print(n3)
