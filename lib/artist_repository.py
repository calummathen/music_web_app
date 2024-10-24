from lib.artist import Artist

class ArtistRepository:
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from artists ORDER BY id ASC')
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row['genre'])
            artists.append(item)
        return artists
    
    
    def find(self, id):
        rows = self._connection.execute('SELECT * from artists WHERE id = %s', [id])
        row = rows[0]
        return Artist(row["id"], row["name"], row['genre'])
    
    def find_with_albums(self, id):
        rows = self._connection.execute('SELECT artists.id as artist_id, '
                                        'artists.name, '
                                        'artists.genre, '
                                        'albums.title, '
                                        'albums.artist_id ' 
                                        'from artists JOIN albums '
                                        'ON artists.id = albums.artist_id '
                                        'WHERE artists.id = %s', [id])
        albums = []
        for row in rows:
            album = row['title']
            albums.append(album)
        object = Artist(rows[0]["artist_id"], rows[0]["name"], rows[0]['genre'])
        object.albums = albums
        return object
    
    def create(self, artist):
        rows = self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s) '
                                 'RETURNING id', [
            artist.name,
            artist.genre
        ])
        row = rows[0]
        artist.id = row["id"]

    def delete(self, id):
        self._connection.execute('DELETE FROM artists WHERE id = %s', [id])

    def update(self, artist):
        self._connection.execute('UPDATE artists SET name = %s, '
                                 'genre = %s '
                                 'WHERE id = %s', 
                                 [artist.name, artist.genre, artist.id])    