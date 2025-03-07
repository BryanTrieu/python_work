filename = 'guest_book.txt'

guest = input('Please input a name for the guest:')

# Greets the guest
print(f"Hello {guest.title()}, thank you for visiting our establishment.")

# Records the guest name in guest.txt
with open(filename, 'a') as file_object:
	file_object.write(f"{guest}\n")
