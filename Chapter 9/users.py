class User():
	def __init__(self,first_name,last_name,gender):
		self.first=first_name
		self.last=last_name
		self.gender=gender
		self.attempts=0
	def describe_user(self):
		print(self.last.title()+' '+self.first.title()+" is a "+
		self.gender)	
	def greet_user(self):
		print("Nice to meet you, "+self.first.title()+' !')
	def increment_login_attempts(self):
		self.attempts+=1
		print("Your number of login is "+str(self.attempts))
	def reset_login_attempts(self):
		self.attempts=0
		print('You have reset the miles to '+str(self.attempts))		
user_1=User('yicheng','hu','male')
user_1.describe_user()
user_1.greet_user()	
user_1.increment_login_attempts()		
user_1.increment_login_attempts()		
user_1.increment_login_attempts()		
user_1.increment_login_attempts()		
user_1.reset_login_attempts()
user_1.increment_login_attempts()		
user_1.increment_login_attempts()		
user_1.increment_login_attempts()		
user_1.increment_login_attempts()
user_1.increment_login_attempts()		
user_1.increment_login_attempts()		
user_1.increment_login_attempts()		
user_1.increment_login_attempts()
print ('\n'+str(user_1.attempts))		


