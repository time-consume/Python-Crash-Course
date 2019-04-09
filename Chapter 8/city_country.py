def city_country(city,country):
	pair={'cities':city,'countries':country}
	print(pair['cities'].title+" is in "+pair['countries'].title)
	return pair
while True:
	print("Please enter a city and the country it belongs to")
	print("or enter q to quit")
	a=input("City Name: ")
	if a=='q':
		break
	b=input("Country Name: ")
	if b=='q':
		break
	city_country(a,b)
	show=city_country(a,b)
	print(show)
	
