requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print ("Adding mushrooms.")
if 'pepporoni' in requested_toppings:
	print ("Adding pepporoni.")
if 'extra cheese' in requested_toppings:
	print ("Adding extra cheese.")

print("\nFinished making your pizza!")

# - 5 Checking for special items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}.")

print("\nFinished making your second pizza!")

# - 5 Checking for empty list
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
else:
	print("\nAre you sure you want a plain pizza?")

# - 5 Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we do not have {requested_topping} available.")

print("\nFinished making your special pizza!")
