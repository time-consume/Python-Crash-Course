def city_country(city,country):
	pair={'ci':city,'co':country}
	return pair
result=city_country(city=['shanghai','beijing'],country=['china','China'])
for i in result.values():
	print(result['ci']+result['co'])
