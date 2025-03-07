# 8-6 city names function22319
def city_country(city, country):
	"""Displays name of a city and country"""
	city_country_pair = f"{city}, {country}"
	return city_country_pair.title()

test = city_country('santiago', 'chile')
print(test)

test2 = city_country('paris', 'france')
test3 = city_country('athens', 'greece')
print(test2)
print(test3)


