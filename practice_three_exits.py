# exercise 7-6 - practice conditional test, active variable, and break steatment

# active variable example
prompt = "Please enter your favorite programming language."
prompt += "\nPlease enter 'quit' when you are finished: "

active = True

while active:
	language = input(prompt)

	if language == 'quit':
		active = False
	if language != 'quit':
		print(f"\nI see you enjoy programming with {language.title()}")

# practice conditional while loop
x = 0
while x <= 5:
	print(x)
	x += 1

# practice for break statement
prompt = "Please enter your favorite foods."
prompt += "\nPlease enter 'quit' when you are finished: "

while True:
	food = input(prompt)

	if food == 'quit':
		break
	else:
		print(f"I see you enjoy eating {food}.")
