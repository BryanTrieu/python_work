# - 5-11 Ordinal numbers exercise
numbers = range(1,10)
print(numbers)

for number in numbers:
	if number == 1:
		print('1st')
	elif number == 2:
		print('2nd')
	elif number == 3:
		print('3rd')
	else:
		print(f"{number}th")