# 10-12 show favorite number using json
import json

def show_favorite_number():
	filename = 'favorite_number.json'
	try:
		with open(filename) as f:
			favorite_num = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return favorite_num

print(show_favorite_number())


