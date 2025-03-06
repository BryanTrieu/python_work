# 6-3 glossary exercises
glossary = {
	'dictionary': 'list of key value pairs',
	'variable': 'a named container that stores a piece of data',
	'list': 'a collection of items in a particular order',
	'tuple': 'a colection of items in a particular order which is not meant to change',
	'key value pair': 'a pair of values found within a dictionary',
	}

print(glossary)

for definition in glossary:
	print(f"\n{definition.title()}:")
	print(f"{glossary[definition]}")

# simpler for statement
for definition, value in glossary.items():
	print(f"\n{definition.title()}:")
	print(f"{value}")

glossary['set'] = 'a collection of items where each item is unique'
glossary['method'] = 'a function associated with an object'
glossary['function'] = 'a block a code which only runs when it is called upon'

# printing additional definitions in the glossary
for definition, value in glossary.items():
	print(f"\n{definition.title()}:")
	print(f"{value}")

# listing all the set values in glossary
print("\nThese are just the set values of glossary:")
for definition in set(glossary.values()):
	print(definition)