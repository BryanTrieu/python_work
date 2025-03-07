# - 8-3 & 8-4 exercises
def make_shirt(message= 'I love python.', size = "L"):
	"""Displays size and message of shirt"""
	print(f"\nThe shirt will be size {size}.")
	print("Text will say: ")
	print(f"\t{message}")
#make_shirt('XL', 'Hello world!')
make_shirt(message= "Pinky, it's time to take over the world!", size= "XXXXS")

make_shirt()
make_shirt(size= 'M')