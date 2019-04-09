favorite_language={'Alice':'Python','Bob':'C','Clement':'R'}
poll=['Alice','Bob','Clement','David','Emma']
for names in favorite_language.keys():
	print(names)
for name in poll:
	if name in favorite_language.keys():
# names is only Clement, favorite_language.keys() is a list
		print("Thank you for taking the poll, "+name)
	else:
		print(name+" ,pls. take the poll")	
