# example of using classes for example 9-1
class Restaurant:
	"""A simple attempt to model if a restaurant is open"""
	
	def __init__(self, restaurant_name, cuisine_type):
		""" initialize name and attributes """
		self.name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		""" function to display name and cuisine type """
		print(f"\nRestaurant name: {self.name}")
		print(f"Type: {self.name}")

	def open_restaurant(self):
		""" function to display message that restaurant is open """
		print(f"\nThe restaurant {self.name} is open.")

my_restaurant = Restaurant('Olive Garden', 'Italian')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()