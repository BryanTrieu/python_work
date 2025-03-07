# Deleted everything within pizza.py to make module as defined on page 150
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f" - {topping}")