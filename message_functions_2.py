# 8-10 messages exercise:  Make a list containing a series of short text messages. Pass the
#  list to a function called show_messages(), which prints each text message

# list of short text messages
message_list = ['Hello there!', 'What are you up to?', 'See you later!']

def show_messages(messages):
	""" Function to show all text messages """
	print("\nThese are the text messages: ")
	for message in messages:
		print(message)

show_messages(message_list)

sent_messages = []
def send_messages(messages):
	""" Function to print messages followed by moving the message to a new list """
	while messages:
		current_message = messages.pop()
		print(current_message)
		sent_messages.append(current_message)

send_messages(message_list[:])
print(f"Message List: {message_list}")
print(f"Sent message list: {sent_messages}")