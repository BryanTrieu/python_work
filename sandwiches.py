# 7-8 deli exercises
sandwich_orders = ['ham', 'pastrami', 'turkey', 'pastrami', 'blt', 'meatball','pastrami']                                                                                                                                                                                                                                      
finished_sandwich = []

while sandwich_orders:
	sandwich= sandwich_orders.pop()
	# 7-9 no pastrami exercise using continue
	if sandwich == 'pastrami':
		print(f"\n I'm sorry, we're out of pastrami.")
		continue
	finished_sandwich.append(sandwich)
	print(f"\nI made your {sandwich} sandwich.")
print(f"\n We made the following sandwiches: ")
for sandwich in finished_sandwich:
	print(f"\t{sandwich}")