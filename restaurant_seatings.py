number_of_guests = input("How many guests will be dining in your party tonight?: ")
number_of_guests = int(number_of_guests)

if number_of_guests > 8:
	print(f"Unfortunately there will be a short wait for a party of {number_of_guests}.")
else:
	print(f"Please come with your party of {number_of_guests}, we can seat you right away.")