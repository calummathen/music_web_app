from playwright.sync_api import Page, expect

def test_get_artists_html(page, test_web_address):
    page.goto(f"http://{test_web_address}/artists")

    h2_tags = page.locator("h2")
    expect(h2_tags.nth(0)).to_have_text("Pixies")

def test_get_artists_links(page, test_web_address):
    page.goto(f"http://{test_web_address}/artists")

    a_tags = page.locator("a:has-text('Go to Artist')")
    first_link = a_tags.nth(0)
    first_link.click()
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Pixies")

def test_get_albums_html(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")

    h2_tags = page.locator("h2")
    expect(h2_tags.nth(0)).to_have_text("Doolittle")

def test_get_albums_links(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")

    # page.wait_for_selector("a")
    go_to_album = page.locator("a:has-text('Go to Album')")
    first_link = go_to_album.nth(0)
    first_link.click()
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Doolittle")

def test_get_albums_4th_link(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")

    # page.wait_for_selector("a")
    go_to_album = page.locator("a:has-text('Go to Album')")
    first_link = go_to_album.nth(3)
    first_link.click()
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Super Trouper")

def test_new_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.fill("input[name='title']", "New Album Pixies")
    page.fill("input[name='release_year']", "1999")
    page.fill("input[name='artist_id']", "1")
    page.click("text=Create Album")

    title_element = page.locator(".album-title")
    expect(title_element).to_have_text("New Album Pixies")

    release_year_element = page.locator(".album-release-year")
    expect(release_year_element).to_have_text("Released in: 1999")

def test_create_album_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.click("text=Create Album")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Title can't be blank, Release Year can't be blank, Artist ID can't be blank")

def test_new_artist(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add a new artist")
    page.fill("input[name='name']", "50 Cent")
    page.fill("input[name='genre']", "Rap")
    page.click("text=Create Artist")

    name_element = page.locator(".artist-name")
    expect(name_element).to_have_text("50 Cent")

    genre_element = page.locator(".artist-genre")
    expect(genre_element).to_have_text("Genre: Rap")

def test_create_album_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add a new artist")
    page.click("text=Create Artist")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Name can't be blank, Genre can't be blank")
