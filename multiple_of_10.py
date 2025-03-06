number = input("Please enter a number and we'll check to see if it's divisible by 10: ")
number = int(number)

if number % 10 == 0:
	print(f"The number {number} is divisible by 10.")
else:
	print(f"The number {number} is not divisible by 10.")
