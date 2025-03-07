# 10-12 program to use json to remember favorite number
import json

def get_stored_number():
	filename = 'favorite_number.json'
	try:
		with open(filename) as f:
			favorite_num = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return favorite_num

def get_favorite_number():
	filename = 'favorite_number.json'
	favorite_num = input("Please enter your favorite number.\n")
	with open(filename, 'w') as f:
		json.dump(favorite_num, f)
	return favorite_num

def show_favorite_number():
	filename = 'favorite_number.json'
	favorite_num = get_stored_number()
	if favorite_num:
		print(f"I know that your favorite number is {favorite_num}!")
	else:
		favorite_num = get_favorite_number()
		print(f"I'll remember that your favorite number is {favorite_num}.")

show_favorite_number()
