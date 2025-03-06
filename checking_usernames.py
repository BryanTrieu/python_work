current_users = ['admin','mark','john','paul','luke']
new_users = ['bart','lisa','homer','luke','PAUL']

for user in new_users:
	if user.lower() in current_users:
		print(f"Sorry, the username {user} is not available. Please try a different username.")
	else:
		print(f"The username {user} is available. Please proceed with signing up.")
