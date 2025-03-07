# Exercise 10-5 programming poll
filename = 'programming_poll_results.txt'
polling_active = True

prompt = "Please tell us what you like about programming.\n"
prompt += "Input q to escape.\n"

while polling_active:
	message = input(prompt)
	if message == 'q':
		polling_active = False
	else:
		with open(filename, 'a') as file_object:
			file_object.write(f"{message}\n")
