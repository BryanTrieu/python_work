"""9-11 import class and modules exercise"""
class User:
	"""Initialize name and attributes"""
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0

	def describe_user(self):
		"""Print user information"""
		print(f"\nUser information: ")
		print(f"\tFirst name: {self.first_name.title()}")
		print(f"\tLast name: {self.last_name.title()}")

	def greet_user(self):
		"""Print a greeting to the user"""
		print(f"\nHello {self.first_name.title()}, thanks for using the program!")

	def increment_login_attempts(self):
		"""Increments login_attempts by 1"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Resets login_attempts attr to 0"""
		self.login_attempts = 0

