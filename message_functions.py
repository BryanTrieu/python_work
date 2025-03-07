# 8-9 messages exercise:  Make a list containing a series of short text messages. Pass the
#  list to a function called show_messages(), which prints each text message

# list of short text messages
message_list = ['Hello there!', 'What are you up to?', 'See you later!']

def show_messages(messages):
	""" Function to show all text messages """
	print("\nThese are the text messages: ")
	for message in messages:
		print(message)

show_messages(message_list)
