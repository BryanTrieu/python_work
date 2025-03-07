user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}

for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

# 9-3 create class users exercise
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

# 9-7 Create Admin class which inherits User class attributes
class Admin(User):
	
	def __init__(self, first_name, last_name):
		"""Init name and attributes including privilege"""
		super().__init__(first_name, last_name)	
		self.privileges = Privileges()

# 9-8 Create Privileges class
class Privileges:
	def __init__(self, privileges=['can add user', 'can del user', 'can ban user']):
		self.privileges = privileges

	def show_privileges(self):
		"""Print privileges that user has"""
		print(f"Admin privileges:")
		for privilege in self.privileges:
			print(f"\t - {privilege}")	

# 9-3 Create instances of class User and call upon both methods fo each user

user_1 = User('enrico', 'fermi')
user_2 = User('albert', 'einstein')
user_3 = User('leslie', 'knope')

user_1.describe_user()
user_2.describe_user()
user_3.describe_user()

user_1.greet_user()
user_2.greet_user()
user_3.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)

# Testing class Admin and its methods
admin_1 = Admin('ron', 'swanson')

admin_1.describe_user()
#admin_1.show_privileges()

# Testing class Admin and Privileges methods
admin_2 = Admin('leslie', 'knope')

admin_2.describe_user()
admin_2.privileges.show_privileges()