def make_album(artist, title):
    """Return a dictionary representing an album."""
    album = {'artist': artist, 'title': title}
    return album

album1 = make_album('The Beatles', 'Abbey Road')
album2 = make_album('Pink Floyd', 'The Dark Side of the Moon')
album3 = make_album('Led Zeppelin', 'IV')
print(album1)
print(album2)
print(album3)

def make_album(artist, title, num_songs=None):
    """Return a dictionary representing an album."""
    album = {'artist': artist, 'title': title}
    if num_songs is not None:
        album['num_songs'] = num_songs
    return album

album1 = make_album('The Beatles', 'Abbey Road', 17)
album2 = make_album('Pink Floyd', 'The Dark Side of the Moon', 10)
print(album1)
print(album2)