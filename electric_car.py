class Car:
	""" A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car. """
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
	
	def read_odometer(self):
		"""Print a statement showing the car's mileage"""
		print(f"The car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading"""
		self.odometer_reading += miles

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

my_car = ElectricCar('audi', 'r5', 2024)
print(my_car.get_descriptive_name())
my_car.battery.describe_battery()
my_car.battery.get_range()

# 9-9 battery upgrade method test
my_car.battery.upgrade_battery()
my_car.battery.get_range()