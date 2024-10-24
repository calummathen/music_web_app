import os
from flask import Flask, request, jsonify, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

@app.route('/home')
def home():
    return "This is home"

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    albums_as_dict = [album.to_dict() for album in albums]
    
    if request.accept_mimetypes['application/json'] >= request.accept_mimetypes['text/html']:
        return jsonify(albums_as_dict)
    
    return render_template('albums.html', albums=albums)

@app.route('/albums/<int:id>', methods=['GET'])
def find_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album_and_artist = repository.find_with_artist(id)
    album = album_and_artist[0]
    artist = album_and_artist[1]
    return render_template('albums.html', albums=[album], artist=artist)


@app.route('/albums', methods=['POST'])
def add_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    if not album.is_valid():
        errors = album.generate_errors()
        return render_template('new-album.html', errors=errors)
    repository.create(album)
    return redirect(f"/albums/{album.id}")

@app.route('/albums/new', methods=['GET'])
def get_album_new():
    return render_template('new-album.html')


@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    artists_as_dict = [artist.to_dict() for artist in artists]

    if request.accept_mimetypes['application/json'] >= request.accept_mimetypes['text/html']:
        return jsonify(artists_as_dict)
    
    return render_template('artists.html', artists=artists)

@app.route('/artists/<int:id>', methods=['GET'])
def get_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.find(id)
    return render_template('artists.html', artists=[artists])

@app.route('/artists', methods=['POST'])
def add_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(None, request.form['name'], request.form['genre'])
    if not artist.is_valid():
        errors = artist.generate_errors()
        return render_template('new-artist.html', errors=errors)
    repository.create(artist)
    return redirect(f"/artists/{artist.id}")

@app.route('/artists/new', methods=['GET'])
def get_artist_new():
    return render_template('new-artist.html')

@app.route('/artist_with_albums', methods=['GET'])
def get_artist_with_albums():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist_with_albums = repository.find_with_albums(1)
    artist_with_albums_to_dict = artist_with_albums.to_dict()
    # artist_with_albums_as_dict = [each.to_dict() for each in artist_with_albums]
    return jsonify(artist_with_albums_to_dict), 200

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

