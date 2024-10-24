from playwright.sync_api import Page, expect # Tests for your routes go here

def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is home'

def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.json == [
        {"artist_id":1,"id":1,"release_year":1989,"title":"Doolittle"},
        {"artist_id":1,"id":2,"release_year":1988,"title":"Surfer Rosa"},
        {"artist_id":2,"id":3,"release_year":1974,"title":"Waterloo"},
        {"artist_id":2,"id":4,"release_year":1980,"title":"Super Trouper"},
        {"artist_id":1,"id":5,"release_year":1990,"title":"Bossanova"},
        {"artist_id":3,"id":6,"release_year":2019,"title":"Lover"},
        {"artist_id":3,"id":7,"release_year":2020,"title":"Folklore"},
        {"artist_id":4,"id":8,"release_year":1965,"title":"I Put a Spell on You"},
        {"artist_id":4,"id":9,"release_year":1978,"title":"Baltimore"},
        {"artist_id":4,"id":10,"release_year":1971,"title":"Here Comes the Sun"},
        {"artist_id":4,"id":11,"release_year":1982,"title":"Fodder on My Wings"},
        {"artist_id":2,"id":12,"release_year":1973,"title":"Ring Ring"}]

def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.post('/albums', data={
        'title': 'Title ADD',
        "release_year": "1999",
        "artist_id": "2"
    })
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.json == [
        {"artist_id":1,"id":1,"release_year":1989,"title":"Doolittle"},
        {"artist_id":1,"id":2,"release_year":1988,"title":"Surfer Rosa"},
        {"artist_id":2,"id":3,"release_year":1974,"title":"Waterloo"},
        {"artist_id":2,"id":4,"release_year":1980,"title":"Super Trouper"},
        {"artist_id":1,"id":5,"release_year":1990,"title":"Bossanova"},
        {"artist_id":3,"id":6,"release_year":2019,"title":"Lover"},
        {"artist_id":3,"id":7,"release_year":2020,"title":"Folklore"},
        {"artist_id":4,"id":8,"release_year":1965,"title":"I Put a Spell on You"},
        {"artist_id":4,"id":9,"release_year":1978,"title":"Baltimore"},
        {"artist_id":4,"id":10,"release_year":1971,"title":"Here Comes the Sun"},
        {"artist_id":4,"id":11,"release_year":1982,"title":"Fodder on My Wings"},
        {"artist_id":2,"id":12,"release_year":1973,"title":"Ring Ring"},
        {"artist_id":2,"id":13,"release_year":1999,"title":"Title ADD"}]

def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.json == [
        {'genre': 'Rock', 'id': 1, 'name': 'Pixies'}, 
        {'genre': 'Pop', 'id': 2, 'name': 'ABBA'}, 
        {'genre': 'Pop', 'id': 3, 'name': 'Taylor Swift'}, 
        {'genre': 'Jazz', 'id': 4, 'name': 'Nina Simone'}
        ]
    
def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.post('/artists', data={
        'name': 'ADD name',
        'genre': "Rock"
    })
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.json == [
        {'genre': 'Rock', 'id': 1, 'name': 'Pixies'}, 
        {'genre': 'Pop', 'id': 2, 'name': 'ABBA'}, 
        {'genre': 'Pop', 'id': 3, 'name': 'Taylor Swift'}, 
        {'genre': 'Jazz', 'id': 4, 'name': 'Nina Simone'},
        {'genre': 'Rock', 'id': 5, 'name': 'ADD name'}
        ]

def test_get_artist_with_albums(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get('/artist_with_albums')
    assert response.status_code == 200
    
    assert response.json == {
        'albums': ['Doolittle', 'Surfer Rosa', 'Bossanova'], 
        'genre': 'Rock', 
        'id': 1, 
        'name': 'Pixies'
        }
    


def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.json ==[
        {'genre': 'Rock', 'id': 1, 'name': 'Pixies'}, 
        {'genre': 'Pop', 'id': 2, 'name': 'ABBA'}, 
        {'genre': 'Pop', 'id': 3, 'name': 'Taylor Swift'}, 
        {'genre': 'Jazz', 'id': 4, 'name': 'Nina Simone'}
        ]
    
