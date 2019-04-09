def make_car(manu,mod,**info):
	car={}
	car['manufacture']=manu
	car['model']=mod
	for key,value in info.items():
		car[key]=value
	return car
c = make_car('subaru', 'outback', color='blue', tow_package=True)
print(c)			
	
	
