names="What's your name?"
question="If you could visit one place in the world,"
question+="Where would you go?"
poll={}
while True:
	name=input(names)
	mark=input(question)
	poll[name]=mark
	repeat=input("do you want to another survey(y/n)?")
	if repeat=='n':
		break
for n,m in poll.items():
	print(n.title()+" wants to go to "+m.title())		
