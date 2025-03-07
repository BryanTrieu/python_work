title = {}
def make_album(artist_name, album_title, no_of_songs=None):
	"""Displays dictionary containing artist name and album title"""
	title = {'artist': artist_name, 'album': album_title,}
	if no_of_songs:
		title['number of songs'] = no_of_songs
	return title

example = make_album('queen', 'queen', 30)
print(example)
example = make_album('led zeppelin', 'stairway to heaven')
print(example)