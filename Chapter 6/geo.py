geo={'egypt':'nile','china':'yangtze','america':'mississippi'}
for country,river in geo.items():
	print("The "+river.title()+" runs through "+country.title())
for country in sorted(geo.keys()):
	print(country.title())
for river in sorted(geo.values()):
	print(river.title())
