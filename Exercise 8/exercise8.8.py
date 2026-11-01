def make_album(artist, title, num_songs=None):
    """Return a dictionary representing an album."""
    album = {'artist': artist, 'title': title}
    if num_songs is not None:
        album['num_songs'] = num_songs
    return album

while True:
    print("\nPlease enter the artist and album title (or 'q' to quit):")
    artist = input("Artist: ")
    if artist.lower() == 'q':
        break
    title = input("Album Title: ")
    if title.lower() == 'q':
        break
    num_songs_input = input("Number of Songs (optional): ")
    if num_songs_input.lower() == 'q':
        break
    num_songs = int(num_songs_input) if num_songs_input else None

    album = make_album(artist, title, num_songs)
    print(f"\nAlbum created: {album}")