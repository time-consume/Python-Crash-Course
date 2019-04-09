cities={
'shanghai':{'country':'china','pop':'2000','facts':'rich'},
'london':{'country':'england','pop':'1000','facts':'fog'},
'cleveland':{'country':'america','pop':'500','facts':'cold'}
}
for city,fact in cities.items():
	print(city.title()+" belongs to "+fact['country'].title()
	+" ,has a population of "+fact['pop']+", and it is "+fact['facts'])
