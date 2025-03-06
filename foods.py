# - Example of copying a list using a slice [:]
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# - Following example will not work.. both food variables will refer to same list:
##	friend_foods = my_foods

for food in my_foods:
	print(food)

for food in friend_foods:
	print(f"\nThey really like {food}.")

