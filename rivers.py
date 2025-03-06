# 6-5 rivers exercises
rivers = {
	'nile': 'africa',
	'mississippi': 'united states',
	'amazon': 'south america',
	}

for river, country in rivers.items():
	print(f"The {river.title()} flows in {country.title()}.")

# printing value of river names
print("\nThe rivers are named:")
for river in rivers:
	print(f"{river.title()} river")

# printing value of location names
print("\nThe rivers are located in:")
for value in set(rivers.values()):
	print(value.title())