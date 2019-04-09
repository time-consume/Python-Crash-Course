def show_content(filename):
	try:
		with open(filename) as content:
			content=content.readlines()
	except FileNotFoundError:
		msg="sorry, the content can bot be found"
		print(msg)
	else:
		for line in content:
			print(line)
show_content('learn.txt')						
