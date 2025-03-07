"""Example of class from chapter 9"""
class Dog:
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate a dog rolling over in response to a command."""
		print(f"{self.name} rolled over!")

# making an instance of a class
my_dog = Dog('Violet', 12)
your_dog = Dog('Lucy', 3)

# prints instance's attributes name and age
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# call method by invoking instance name
my_dog.sit()
my_dog.roll_over()

# print second instace's attribute
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()