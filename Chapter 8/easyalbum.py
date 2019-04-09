def make_album(music,artist,track=''):
	album={'musics':music,'artists':artist,'tracks':track}
	return album
anyway=make_album('a','b')
print(anyway)
anyway=make_album('c','d')
print(anyway)
anyway=make_album('e','f','2')
print(anyway)
