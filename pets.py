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

# chapter 7 example of while loop
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)

# - Example of functions in chapter 8
def describe_pet(pet_name, animal_type= 'dog'):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name= 'harry', animal_type= 'hamster')

describe_pet(pet_name= 'willie')
describe_pet('willie')
describe_pet('harry', 'hamster')