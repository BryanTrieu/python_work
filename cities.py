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

# - chapter 7 example of using break to exit a loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}.")

