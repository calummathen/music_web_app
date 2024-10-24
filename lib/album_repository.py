from lib.album import Album

class AlbumRepository:
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from albums ORDER BY id ASC')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    

    def find(self, id):
        rows = self._connection.execute('SELECT * from albums WHERE id = %s', [id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
    
    def find_with_artist(self, id):
        rows = self._connection.execute('SELECT albums.id AS album_id, '
                                        'albums.title, '
                                        'albums.release_year, '
                                        'albums.artist_id, '
                                        'artists.name '
                                        'FROM albums JOIN artists '
                                        'ON albums.artist_id = artists.id '
                                        'WHERE albums.id = %s', [id])
        row = rows[0]
        album = Album(row["album_id"], row["title"], row["release_year"], row["artist_id"])
        artist = row['name']
        return [album, artist]
    
    def create(self, album):
        rows = self._connection.execute('INSERT INTO albums (title, release_year, artist_id) '
                                 'VALUES (%s, %s, %s) RETURNING id', [
            album.title, album.release_year, album.artist_id
        ])
        row = rows[0]
        album.id = row["id"]
        return album

    def delete(self, id):
        self._connection.execute('DELETE FROM albums WHERE id = %s', [id])

    def update(self, album):
        self._connection.execute('UPDATE albums SET title = %s, '
                                 'release_year = %s, '
                                 'artist_id = %s '
                                 'WHERE id = %s', 
                                 [album.title, album.release_year, album.artist_id, album.id])    