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

# 8-8 user albums exercise
user_polling = True
while user_polling:
	name = input(f"\nPlease input a band or artist name: ")
	album = input(f"Please input an album from the band or artist: ")
	example = make_album(name, album)
	print(example)
	restart = input(f"Would you like to continue? y/n ")
	if restart == 'n':
		user_polling = False