from lib.artist_repository import ArtistRepository
from lib.artist import Artist

def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)

    artists = repository.all()

    assert artists ==[
        Artist(1, 'Pixies', 'Rock'), 
        Artist(2, 'ABBA', 'Pop'), 
        Artist(3, 'Taylor Swift', 'Pop'), 
        Artist(4, 'Nina Simone', 'Jazz')
    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)

    artist = repository.find(1)
    assert artist == Artist(1, 'Pixies', 'Rock')


def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist(None, "Testadd", "TestGen"))

    artists = repository.all()
    assert artists ==[
        Artist(1, 'Pixies', 'Rock'), 
        Artist(2, 'ABBA', 'Pop'), 
        Artist(3, 'Taylor Swift', 'Pop'), 
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, "Testadd", "TestGen")
    ]

def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    repository.delete(3) 

    artists = repository.all()
    assert artists ==[
        Artist(1, 'Pixies', 'Rock'), 
        Artist(2, 'ABBA', 'Pop'),  
        Artist(4, 'Nina Simone', 'Jazz')
    ]

def test_update_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artist = repository.find(3)
    artist.name = 'Updated Swift'
    repository.update(artist)

    artists = repository.all()
    assert artists ==[
        Artist(1, 'Pixies', 'Rock'), 
        Artist(2, 'ABBA', 'Pop'), 
        Artist(3, 'Updated Swift', 'Pop'), 
        Artist(4, 'Nina Simone', 'Jazz')
    ]

def test_find_artist_with_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    result = repository.find_with_albums(1)

    assert result == Artist(1, 'Pixies', 'Rock', [
        'Doolittle',
        'Surfer Rosa',
        'Bossanova'
    ])
    