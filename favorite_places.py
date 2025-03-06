favorite_places = {
	'mark': 'jerusaleum',
	'john': 'bethlehem',
	'luke': 'corinthia',
	'paul': 'israel',
	}

for person, place in favorite_places.items():
	print(f"{person.title()}'s favorite place is {place.title()}.")
