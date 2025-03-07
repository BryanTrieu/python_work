# example of using classes for example 9-1
class Restaurant:
	"""A simple attempt to model if a restaurant is open"""
	
	def __init__(self, restaurant_name, cuisine_type):
		""" initialize name and attributes """
		self.name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Method to display name and cuisine type """
		print(f"\nRestaurant name: {self.name.title()}")
		print(f"Type: {self.cuisine_type.title()}")

	def open_restaurant(self):
		"""Method to display message that restaurant is open """
		print(f"\nThe restaurant {self.name.title()} is open.")

	def set_number_served(self, served):
		"""Method to set number of customers served"""
		self.number_served = served

	def increment_number_served(self, add_served):
		"""Method to increment number of customers served"""
		self.number_served += add_served 

class IceCreamStand(Restaurant):
	"""A simple attempt to model an ice cream stand."""

	def __init__(self, restaurant_name, cuisine_type='Dessert'):
		"""Initialize attributes"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['vanilla', 'chocolate', 'strawberry']

	def describe_flavors(self):
		"""Prints ice cream flavors"""
		print(f"\nIce cream flavors available:")
		for flavor in self.flavors:
			print(f" - {flavor.title()}")

# create instance restaurant of class Restaurant
restaurant = Restaurant('olive garden', 'italian')

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2 three restaurant instances exercise
my_restaurant = Restaurant('del taco', 'mexican')
your_restaurant = Restaurant('panda express', 'chinese')
his_restaurant = Restaurant('jack in the box', 'fast food')

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
his_restaurant.describe_restaurant()

# Example of manually updating an instance value
print(restaurant.number_served)
restaurant.number_served = 100_000
print(restaurant.number_served)

# Example of using methods to update an instance value
your_restaurant.set_number_served(100)
print(your_restaurant.number_served)
your_restaurant.increment_number_served(10_000)
print(your_restaurant.number_served)

# 9-6 Test Ice Cream Class
ice_cream_restaurant = IceCreamStand("baskin robbins")
ice_cream_restaurant.describe_restaurant()
ice_cream_restaurant.describe_flavors()