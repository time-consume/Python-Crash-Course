import pygal
from random import randint

class Die():
	def __init__(self,num_sides=6):
		self.num_sides=num_sides
	def roll(self):
		return randint(1,self.num_sides)
				
my_die_1=Die()
my_die_2=Die()
results=[]
frequencies=[]

for roll_num in range(1,10000):
	result=my_die_1.roll()+my_die_2.roll()
	results.append(result)
	
max_result=	my_die_1.num_sides+my_die_2.num_sides

for value in range(2,max_result+1):
	frequency=results.count(value)
	frequencies.append(frequency)

hist=pygal.Bar()
hist.title='Results of rooling 10000 times'
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title='Result'
hist.y_title='Frequency of labels'
hist.add('D6+D6',frequencies)
hist.render_to_file('die_visual.svg')	
