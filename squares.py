squares = []
for value in range(1, 11):
	squares.append(value ** 2)
print(squares)

# List Comprehension method to calculate squares using variable number instead of value
squares = [number**2 for number in range(1, 11)]
print(squares)