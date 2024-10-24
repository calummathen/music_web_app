from lib.artist import Artist

def test_artist_constructs(db_connection):
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"


def test_artist_formats_nicely(db_connection):
    artist = Artist(1, "Test Artist", "Test Genre")
    assert str(artist) == "Artist(1, Test Artist, Test Genre)"

def test_artists_are_equal(db_connection):
    album1 = Artist(1, "Test Artist", "Test Genre")
    album2 = Artist(1, "Test Artist", "Test Genre")
    assert album1 == album2