from db.run_sql import run_sql

from models.album import Album

def save(album):
    sql = "INSERT INTO albums (title, genre, artist) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist]

    results = run_sql(sql, values)
    id = results[0]["id"]
    album.id = id
    return album

# def select_all():
#     albums = []

#     sql = "SELECT * FROM albums"
#     results = run_sql(sql)

#     for row in results:
#         album = Album(row['title'], row['genre'], row['artist'])
#         albums.append(album)
#     return albums