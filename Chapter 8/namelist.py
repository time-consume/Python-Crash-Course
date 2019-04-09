def build_name(first_name,last_name,age=''):
	person={'first':first_name,'last':last_name}
	if age:
		person['age']=age
	return person
genius=build_name('Yicheng','Hu',22)	
print(genius)
