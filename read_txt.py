filenames = ['cat.txt', 'cats.txt', 'dog.txt', 'dogs.txt']

for file in filenames:
	try:
		with open(file, encoding='utf-8') as f:
			content = f.read()
			print(f'\nReading contents from {file}')
			print(content)
	except FileNotFoundError:
		#print(f"The file {file} does not exist.")
		pass