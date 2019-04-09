class Car():
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0
	def description(self):
		full=str(self.year)+' '+self.make+' '+self.model
		return full.title()
	def reading(self):
		print("This car has "+str(self.odometer_reading)+" miles on it.")
	def update(self,mile):
		if mile >=self.odometer_reading:
			self.odometer_reading=mile
		else:
			print("You got a wrong value for renewal")
	def increment(self,miles):
		self.odometer_reading += miles				
		
			
class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.batt=100
	def des_batt(self):
		fullname=str(self.year)+' '+self.make+' '+self.model
		print(fullname.title()+" has a battery of "+str(self.batt))	


class Battery(ElectricCar):
	def __init__(self,make,model,year,battery):
		super().__init__(make,model,year)
		self.battery=battery
	def des_battery(self):
		fullname=str(self.year)+' '+self.make+' '+self.model
		print(fullname.title()+" has a "+self.battery +" battery of "+str(self.batt)+" kwh.")			

