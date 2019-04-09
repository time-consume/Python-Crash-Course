with open('guest.txt','a') as object:
	checking=True
	namelist=[]
	while checking:
		with open('guest.txt','r') as reading:	
			content=reading.read()
		greeting='\nWelcome to our hotel!\n'
		greeting+='Pls enter the next guest name: \n'
		success='Checked in successfully!\n'
		failure='We already have your name!'
		name=input(greeting)
		if name in namelist:
			print(failure)
		else:	
			if name in content:
				print(failure)
			else:
				print(success)
				object.write(name+'\n')				
				namelist.append(name)
		finish='If that was your last guest, print space to end,print enter to continue'
		end=input(finish)
		if end==' ':
			print("Thank you, we have recorded all the guests")
			print(namelist)
			break
		else:
			continue
				
			
		
