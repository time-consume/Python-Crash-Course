def build_name(first_name,last_name,middle_name=''):
	if middle_name:
		full_name=first_name+" "+middle_name+" "+last_name
		print(full_name.title())
	else:
		full_name=first_name+" "+last_name
		print(full_name.title())
build_name('yicheng','hu','von')			
