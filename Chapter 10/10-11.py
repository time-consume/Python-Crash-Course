import json
a=input("enter a letter: ")
store='s.json'
with open(a,'w') as f_obj:
	json.dump(a,f_obj)
	print("We'll remember you when you come back!")
