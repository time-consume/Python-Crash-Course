with open('learn.txt') as object:
	content=object.read()
	print(content)

with open('learn.txt') as object:
	content=object.read()
	for line in content:
		print('\t'+line)

with open('learn.txt') as object:
	for line in object:
		print('\t'+line)

with open('learn.txt') as object:
	lines=object.readlines()
	str=''
	for line in lines:
		str+=line
print('\t'+str)
