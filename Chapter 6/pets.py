alice={'name':'cat','owner':'adam'}
boy={'name':'dog','owner':'bob'}
cris={'name':'fish','owner':'clement'}
pets=[alice,boy,cris]
for pet in pets:
	for a,b in pet.items():
		print(a,b)
	
