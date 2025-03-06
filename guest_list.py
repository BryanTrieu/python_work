# - 3-4 Guest List exercise
guest_list = ['zvi', 'luffy', 'zorro']
message = f'Hi {guest_list[0].title()}, would you like to come to dinner?'
print(message)
message = f'Hi {guest_list[1].title()}, would you like to come to dinner?'
print(message)
message = f'Hi {guest_list[2].title()}, would you like to come to dinner?'
print(message)

# - 3-5 Changing guest list exercise
print(f'Unfortunately, {guest_list[0].title()} will not be able to make it.')
guest_list[0] = 'nami'
message = f'Hi {guest_list[0].title()}, would you like to come to dinner?'
print(message)
message = f'Hi {guest_list[1].title()}, would you like to come to dinner?'
print(message)
message = f'Hi {guest_list[2].title()}, would you like to come to dinner?'
print(message)

# - 3-6 More Guests exercise
print('We found a bigger table!')
guest_list.insert(0, 'usopp')
guest_list.insert(2, 'chopper')
guest_list.append('robin')
print(guest_list)
message = f'Hi {guest_list[0].title()}, would you like to come to dinner?'
print(message)
message = f'Hi {guest_list[1].title()}, would you like to come to dinner?'
print(message)
message = f'Hi {guest_list[2].title()}, would you like to come to dinner?'
print(message)
message = f'Hi {guest_list[3].title()}, would you like to come to dinner?'
print(message)
message = f'Hi {guest_list[4].title()}, would you like to come to dinner?'
print(message)
message = f'Hi {guest_list[5].title()}, would you like to come to dinner?'
print(message)

# - 3-7 Shrinking Guest list.  NOTE - I think it wants us to use the remove method for the del portion?  del wasn't mentioned in the chapter
print('We can only fit two guests!')
guest_apology = guest_list.pop()
message = f'I\'m sorry {guest_apology.title()}, we can only fit two people on the table.  Maybe next time.'
print(message)
guest_apology = guest_list.pop()
message = f'I\'m sorry {guest_apology.title()}, we can only fit two people on the table.  Maybe next time.'
print(message)
guest_apology = guest_list.pop()
message = f'I\'m sorry {guest_apology.title()}, we can only fit two people on the table.  Maybe next time.'
print(message)
guest_apology = guest_list.pop()
message = f'I\'m sorry {guest_apology.title()}, we can only fit two people on the table.  Maybe next time.'
print(message)
message = f'You\'re still coming to dinner, right {guest_list[0].title()}?'
print(message)
message = f'You\'re still coming to dinner, right {guest_list[1].title()}?'
print(message)
del guest_list[0]
#or guest_list.remove(guest_list[0])
del guest_list[0]
print(guest_list)