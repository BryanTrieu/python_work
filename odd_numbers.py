# - 4-6 Odd Numbers
values = range(1,20,2)
for value in values:
	print (value)

# - 4-7 Threes Exercises
threes = []
for value in range (1, 11):
	threes.append(value * 3)
print(threes)

# - 4-8 Cubes exercises
cubes = []
for value in range (1,11):
	cubes.append(value ** 3)
print(cubes)

# - 4-9 Cube Comprehension
cube_compehensive_list = [value ** 3for value in range (1,11)]
print(cube_compehensive_list)