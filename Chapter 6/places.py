places=['kyoto','osaka','hemeji']
people=['a','b','c']
favorite_places={'a':['osaka'],'b':['kyoto','osaka'],'c':['kyoto','hemeji']}
for people,places in favorite_places.items():
	if len(places)<2:
		print("\t"+people.title()+"'s fabortie places is")
		for p in places:
			print("\t"+p.title())
	else:		
		print("\t"+people.title()+"'s fabortie places are")
		for p in places:
			print("\t"+p.title())
