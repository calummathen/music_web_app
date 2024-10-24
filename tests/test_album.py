from lib.album import Album

def test_album_constructs(db_connection):
    album = Album(1, "Test Album", 1999, 2)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == 1999
    assert album.artist_id == 2

def test_album_formats_nicely(db_connection):
    album = Album(1, "Test Album", 1999, 2)
    assert str(album) == "Album(1, Test Album, 1999, 2)"

def test_albums_are_equal(db_connection):
    album1 = Album(1, "Test Album", 1999, 2)
    album2 = Album(1, "Test Album", 1999, 2)
    assert album1 == album2

def test_album_validity():
    assert Album(1, "", "", 1).is_valid() == False
    assert Album(1, "Title", "", 1).is_valid() == False
    assert Album(1, "", 1999, 1).is_valid() == False
    assert Album(1, "Title", None, 1).is_valid() == False
    assert Album(1, None, 1999, 1).is_valid() == False
    assert Album(1, "Title", 1999, 1).is_valid() == True
    assert Album(None, "Title", 1999, 1).is_valid() == True
    assert Album(1, "Title", 1999, None).is_valid() == False
    assert Album(None, "Title", 1999, "").is_valid() == False