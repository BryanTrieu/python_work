# - Example of sort and reverse sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# - Example of using the temporary sorted function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# - Example of the reverse function
print(cars)
cars.reverse()
print(cars)
count_cars = len(cars)
print(f'I own {count_cars} cars currently.')

# - 5. Example of if statement 
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
