# 8-13 user profile exercise - Build a
#  profile of yourself by calling build_profile(), using your first and last names
#  and three other key-value pairs that describe you.
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein',
							location='princeton',
							field='physics')

print(user_profile)

user_profile = build_profile('bryan', 'trieu',
							location='california',
							field='computer science')
print(user_profile)