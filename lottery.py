from random import choice

# 9-14 Exercise.  Created a tuple of 10 winning numbers and letters 

lottery_possible = (1, 3, 6, 4, 9, 'c', 'x', 'b', 'n', 'w')
winning_ticket = []

while len(winning_ticket) < 4:
	winning_ticket.append(choice(lottery_possible))

print(winning_ticket)

print("If you have the following numbers or letters in your lottery ticket, you win a prize!")
for char in winning_ticket:
	print(f"\t{char}")

# Create test loop to model how many tickets it'll take to win
loop_counter = 0
loop_active = True
my_ticket = []
while loop_active:
	#Create my ticket
	while len(my_ticket) < 4:
		my_ticket.append(choice(lottery_possible))
	loop_counter += 1
	if my_ticket == winning_ticket:
		print(f"You got the winning ticket! That took {loop_counter} tries.")
		loop_active = False
	else:
		my_ticket = []
		continue
print(f"Winning ticket is {my_ticket}")