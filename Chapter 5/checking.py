current_users=['Alice','Beck','Celman','FriedMan','GraHam']
current_user=[]
for users in current_users:
	users=users.lower()
	current_user.append(users)	
print(current_user)		
new_users=['Eric','Bob','Adam','friedman','graham']
for users in new_users:
	if users.lower() in current_user:
		print("you need to enter a new name")
	else:
		print(users)
