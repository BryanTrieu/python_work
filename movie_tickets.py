prompt = "Please input your age for the correct ticket price."
prompt += "\nPlease input 'quit' when you are done entering all ages: "

while True:
	age = input(prompt)
	
	if age == 'quit':
		break
	age = int(age)

	if age < 3:
		price = 0
	elif 12 >= age >= 3:
		price = 10
	else:
		price = 15
	print(f"The ticket price is ${price}.")