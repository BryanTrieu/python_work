import random

# - 5-8 Hello Admin exercise
users = ['admin','mark','john','paul','luke']
user = users[random.randint(0,4)]

if user == 'admin':
	print('Hello admin, would you like to see the status report?')
else:
	print(f"Hello {user.title()}, thank you for logging in again.")

# - 5-9 - no users exercise
#users = [] # Uncomment to test empty no users test below
if users:
	print(f"Our user list is {users}")
else:
	print("We need to find some users!")
