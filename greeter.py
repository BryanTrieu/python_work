# introduction to inputs
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

# defining a function
def greet_user():
	"""Display a simple greeting."""
	print("Hello!")

greet_user()

# passing information to function
def greet_user(username):
	"""Display a simple greeting."""
	print(f"Hello, {username.title()}!")
greet_user('jesse')

# function to display message
def display_message():
	"""Displays message regarding learning about functions"""
	print("I learned about functions in chapter 8!")

display_message()

# 8-2 Favorite Book function example
def favorite_book(title):
	print(f"One of my favorite books is {title.title()}.")
title = 'Alice in Wonderland'
favorite_book(title)
<<<<<<< HEAD
=======

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

while True:
	print("\nPlease tell me your name: ")
	print("(enter 'q' at any time to quit)")

	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}!")
>>>>>>> fbaf90f (Committing with different email.)
