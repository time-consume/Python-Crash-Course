with open('learn.txt') as object:
	lines=object.readlines()
	for line in lines:
		lin=line.replace('python','java')
		print(lin)


