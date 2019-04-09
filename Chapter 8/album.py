def make_album(music,artist,track=''):
	album={'musics':music,'artists':artist,'tracks':track}
	return album
while True:
	print("Welcome to the poll!")
	print("Enter q to quit")
	a=input("What's your favourite album ?")
	if a=='q':
		break	
	b=input("Who made that music ?")
	if b=='q':
		break	
	c=input("If known, what's the number of track of that album, otherwise, just enter nothing")
	list=make_album(a,b,c)
	print(list)
			
