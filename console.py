import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository

album1 = Album("Jolene", "Country", "Dolly Parton")
album_repository.save(album1)


pdb.set_trace()

