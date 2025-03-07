"""A die that can be used to represent a randomisation"""
from random import randint

class Die:
	def __init__(self, sides=6):
		"""Initialize die attributes"""
		self.sides = sides

	def roll_die(self):
		"""Rolls the die and returns a value."""
		self.value = randint(1, self.sides)
		return self.value

# Test roll_die method 10 times
die = Die()
x = 0

print('6 sided die results:')
while x < 10:
	print(die.roll_die())
	x += 1

ten_die = Die(10)
x = 0
print('\n10 sided die results:')
while x < 10:
	print(ten_die.roll_die())
	x += 1

twenty_die = Die(20)
x = 0
print('\n20 sided die results:')
while x < 10:
	print(twenty_die.roll_die())
	x += 1