responses = {}

# set flag for active
polling_active = True

while polling_active:
	name = input("What is your name?")
	response = input("If you could visit one place in the world, where would you go? ")

	# Stores the name and response as a key-value pair in the responses dictionary
	responses[name] = response

	# Repeat until no or n inputted
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no' or repeat == 'n':
		polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name.title()} would like to travel to {response.title()}.")