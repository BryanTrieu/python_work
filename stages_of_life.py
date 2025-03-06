#Import random module to set age.
import random

# - 5-6 stages of life exercises using consecutive if statements
age = random.randint(1,80)

if age < 2:
	print ('The subject matter is a baby.')
if 4 > age >= 2:
	print ('The subject matter is a toddler.')
if 13 > age >= 4:
	print ('The subject matter is a kid.')
if 20 > age >= 13:
	print ('The subject matter is a teenager.')
if 65 > age >= 20:
	print ('The subject matter is an adult.')
if age >= 65:
	print ('The subject matter is a senior.')
