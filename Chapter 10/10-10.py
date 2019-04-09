def count(filename):
	with open(filename) as content:
		content=content.read()
		number=content.lower().count('the')
		print(number)
count('learn.txt')
