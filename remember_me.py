import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
# Note there's a bug in the book on line 30: book is missing "username = ..." so the print statement will return "None" if the json is missing.
def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	filename = 'username.json'
	username = input("What is your name? ")
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username	

def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		prompt = (f"Is {username} the correct username? y/n\n")
		prompt += ("Default is yes / y: ")
		check_username = input(prompt)

		if check_username == 'n':
			username = get_new_username()
			print(f"We'll remember when you come back, {username}!")
		else:
			print(f"Welcome back, {username}!")
	else:
		username = get_new_username()
		print(f"We'll remember when you come back, {username}!")

greet_user()