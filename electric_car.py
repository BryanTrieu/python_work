"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery:
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement that describes the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		"""Check battery size and upgrade if below 100 kWh"""
		if self.battery_size < 100:
			print(f"Upgrading battery from {self.battery_size} to a 100-kWh battery.")
			self.battery_size = 100
		else:
			print(f"Your battery is already at the maximum size.")

class ElectricCar(Car):
	"""Represents aspects of a car, specific to elctric vehicles."""

	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model, year)
		self.battery = Battery()

