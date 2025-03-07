"""example of using classes for example 9-10"""

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
