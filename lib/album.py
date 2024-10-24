class Album:
    
    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id


    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year,
            'artist_id': self.artist_id
        }
    
    def is_valid(self):
        if self.title and self.release_year and self.artist_id:
            return True
        else:
            return False
        
    def generate_errors(self):
        # errors = ""
        if not self.is_valid():
            errors = "Title can't be blank, Release Year can't be blank, Artist ID can't be blank"
        return errors

    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    