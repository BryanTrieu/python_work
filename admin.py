"""module for class admin and its privileges"""
from user import User

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

