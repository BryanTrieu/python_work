filename = 'learn_python.txt'
with open(filename) as file_object:
	contents = file_object.read()
print('Print contents directly from reading file_object:')
print(contents.replace('Python', 'C'))

print('Printing lines by looping over lines in the file_object:')
with open(filename) as file_object:
	for line in file_object:
		print(line.replace('Python', 'C'))

with open(filename) as file_object:
	lines = file_object.readlines()

print('\nPrinting lines by looping through list:')
for line in lines:
	print(line.strip().replace('Python','C'))
print('\nShow that lines is still a list:')
print(lines)

