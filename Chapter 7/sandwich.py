print("Deli is out of pastrami")
sandwich_orders=['tuna','cheese','egg','pastrami','pastrami','pastrami',]
while 'pastrami'in sandwich_orders:
	sandwich_orders.remove('pastrami')
finished_sandwiches=[]
while set(sandwich_orders):
	progress=sandwich_orders.pop()
	print("your "+progress+" is being processed")
	finished_sandwiches.append(progress)
for sand in finished_sandwiches:
	print(sand+" is finished")
