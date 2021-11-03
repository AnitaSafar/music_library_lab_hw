import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


album_repository.delete_all()
artist_repository.delete_all()

album1 = Album("Jolene", "Country", "Dolly Parton")
album_repository.save(album1)
album2 = Album("9 to 5", "Country", "Dolly Parton")
album_repository.save(album2)
album3 = Album("Jazz", "Hard rock", "Queen")
album_repository.save(album3)

artist1 = Artist("Dolly M. Parton")
artist_repository.save(artist1)
artist2 = Artist("Queen")
artist_repository.save(artist2)

albums = album_repository.select_all()
for album in albums:
    print(album.__dict__)

artists = artist_repository.select_all()
for artist in artists:
    print(artist.__dict___)

pdb.set_trace()

