pets = {
	'pet_1': {
		'name': 'violet',
		'owner': 'bryan',
		'type': 'dog',
		},
	'pet_2': {
		'name': 'milo',
		'owner': 'katie',
		'type': 'cat',
		},
	'pet_3': {
		'name': 'chopper',
		'owner': 'strawhat pirates',
		'type': 'reindeer',
		},
	}

# prints all pet and key-value pairs
for pet in pets.items():
	print(pet)

# prints all pet and key values with formatted text
for pet, value in pets.items():
	print(f"Pet name:")
	print(f"\t{pet}{value['name'].title()}")
	print(f"Owner:")
	print(f"\t{value['owner'].title()}")
	print(f"Type:")
	print(f"\t{value['type'].title()}")


# - Example of different formatting
for pet, value in pets.items():
	print(pet.title())
	name = value['name']
	owner = value['owner']
	type = value['type']
	print(f"\tName: {name.title()}")
	print(f"\tOwner: {owner}")
	print(f"\tType: {type.title()}")