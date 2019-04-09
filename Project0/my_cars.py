"""import classes to the main program"""
from car import Car
from car import ElectricCar
from car import Battery
"""Uses instances and objects in Car"""
my_car=Car('b m w','320i',2008)
print(my_car.description())
print(my_car.make.title())
"""Uses instances and objects in ElectricCar"""
my_volks=ElectricCar('audi','r8',2018)
my_volks.des_batt()
print(my_volks.model.title())
"""Uses instances and objects in Battery"""
my_tesla=Battery('tesla','model s',2018,'Lithian')
my_tesla.des_battery()
print(my_tesla.model.title())
