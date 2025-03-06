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
