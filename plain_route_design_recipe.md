
## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

```

## 2. Create Examples as Tests

```python

# GET /albums
#  Parameters: None

#  Expected response (200 OK):
#  Return a list of all the albums 

# POST /albums
#  Parameters:
#    title: Voyage
#    release_year: 2022
#    artist_id: 2

#  Expected response (200 OK):


# POST /submit
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide an album title, release year and artist_id
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```

