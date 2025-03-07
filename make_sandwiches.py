def make_sandwiches(type, *args):
	"""  Display the type of sandwich and toppings """
	print(f"We are making you a {type} sandwich with the following toppings: ")
	for arg in args:
		print(f" - {arg}")

make_sandwiches('ham', 'cheese', 'mayo', 'salt', 'pepper')
make_sandwiches('meatball', 'cheese')
make_sandwiches('blt')
