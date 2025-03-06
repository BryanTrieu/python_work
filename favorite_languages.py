# example of dictionary of similar objects
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

# example of calling on a key value
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# example of looping through a dictionary
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

# example of keys (name only) vs items (values included)
for name in favorite_languages.keys():
#for name in favorite_languages:	# same without calling keys()
	print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages:
	print(name.title())

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}")

if 'erin' not in favorite_languages:
	print('Erin, please take our poll!')

for name in sorted(favorite_languages):
	print(f"{name.title()}, thank you for taking our poll.")


print('\nThe following languages were mentioned in the poll:')
for language in favorite_languages.values():
	print(language.title())

# example of using set to remove duplicate values
print('\nThe following languages were mentioned in the poll:')
for language in set(favorite_languages.values()):
	print(language.title())

# Braces {} but no key-value pairs means the data is likely a set. Example below:
language = {'python', 'ruby', 'python', 'c'}
print(language)

# 6-6 polling exercises
new_respondent = ['big head','gilfoyle','erlich','sarah']
for respondent in new_respondent:
	# checks if new respondent has already taken the poll
	if respondent in set(favorite_languages):
		print(f"Thank you {respondent.title()} for taking the poll.")
	else:
		print(f"Please take the favorite programming language poll {respondent.title()}. Your input is greatly appreciated.")

# 6 list in a dictionary example
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")
