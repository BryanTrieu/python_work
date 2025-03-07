filenames = ['alice.txt', 'moby_dick.txt', 'little_women.txt']

word = input('Please input the word which we will count within the files. ')

for file in filenames:
	try:
		with open(file) as f:
			content = f.read()
			word_count = content.lower().count(word)
		print(f"The {file} has the word '{word}' in it {word_count} times.")
	except FileNotFoundError:
		print(f"The {file} does not exist.")