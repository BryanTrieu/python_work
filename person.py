person_0 = {}
person_0['first_name'] = 'caitlyn'
person_0['last_name'] = 'tsar'
person_0['age'] = 22
person_0['city'] = 'piltover'

print(person_0)

favorite_numbers = {
	'mark': [1,2],
	'john': 2,
	'paul': 3,
	'luke': 4,
	'galavant': [9,10],
	}



for number in favorite_numbers:
	print(f"{number.title()}'s favorite number is {favorite_numbers[number]}.")

for number in favorite_numbers['mark']:
	print(f"Mark's favorite numbers are {number}")

person_1 = {
	'first_name': 'jinx',
	'last_name': 'pow',
	'age': 16,
	'city': 'zaun',
	}

person_2 = {
	'first_name': 'ekko',
	'age': 17,
	'city': 'zaun'
}

people = [person_0, person_1, person_2]

for person in people:
	print(person)