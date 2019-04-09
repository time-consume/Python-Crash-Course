class Rest():
	def __init__(self,name,type):
		self.name=name
		self.type=type
	def open_rest(self):
		print("Restaurant is opening today!")
	def	des_rest(self):
		print(self.name+" provides with "+self.type+" dishes")
restarant_1=Rest('Hunan','Spicy')
restarant_2=Rest('Shanghai','desert')
restarant_3=Rest('Guangxi','Mushu')
restarant_1.des_rest()
restarant_2.des_rest()
restarant_3.des_rest()


