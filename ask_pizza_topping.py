prompt = "Please enter which pizza toppings you would like."
prompt += "\nPlease enter 'quit' when you are finished: "

while True:
	toppings = input(prompt)
	if toppings == 'quit':
		break
	else:
		print(f"We will add {toppings} to your pizza.")
