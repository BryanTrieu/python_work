# - 5-7 - Example asks to make 5 if statemetns. Going to use recursive loop of test_fruits list instead of multiple if statements.
favorite_fruits = ('cherries','strawberries','mango')
test_fruits = ('pineapples','cherries','strawberries','guava','mango')

for fruit in test_fruits:
	if fruit in favorite_fruits:
		print (f"You really love {fruit}!")
	else:
		print (f"You like but don't love {fruit}.")