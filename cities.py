cities = {
	'anaheim': {
		'county': 'orange',
		'population': 340512,
		'fact': 'disneyland is located in anaheim',
		},
	'yorba linda': {
		'county': 'orange',
		'population': 66147,
		'fact': 'yorba linda is a bird sanctuary',
		},
	'placentia': {
		'county': 'orange',
		'population': 52192,
		'fact': 'placentia is a bedroom community',
		},
	}

for city in cities.items():
	print(city)

# - Example of different formatting
for city, value in cities.items():
	print(city.title())
	county = value['county']
	population = value['population']
	fact = value['fact']
	print(f"\tCounty: {county.title()}")
	print(f"\tPopulation: {population}")
	print(f"\tFact: {fact.title()}")