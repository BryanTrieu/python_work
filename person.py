person = {}
person['first_name'] = 'katie'
person['last_name'] = 'tseng'
person['age'] = 38
person['city'] = 'mission viejo'

print(person)

favorite_numbers = {
	'mark': 1,
	'john': 2,
	'paul': 3,
	'luke': 4,
	'galavant': 9,
	}

for number in favorite_numbers:
	print(f"{number.title()}'s favorite number is {favorite_numbers[number]}.")