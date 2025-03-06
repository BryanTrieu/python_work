# - Exercise from Chapter 7 User Inputs and Loops
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."


#message = ""
#while message != 'quit':
#	message = input(prompt)
	
	#if message != 'quit':
	#	print(message)

## Example of using flag "active" to run the loop.
active = True
while active:
	message = input(prompt)

	if message == 'quit'
		active = False
	else:
		print(message)
