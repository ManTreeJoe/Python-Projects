def make_album(artist_name, album_name, num_songs= None):
    
    album = {'artist': artist_name.title(), 'album': album_name.title(), 'number of songs': num_songs}

    print(album)

make_album('John Mayor', 'Continuum')
make_album('Daryl Hall', 'Bigger Than Both of Us')
make_album('Red Hot Chili Peppers', "Californication", 18)


