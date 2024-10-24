class Artist:
    
    def __init__(self, id, name, genre, albums = []):
        self.id = id
        self.name = name
        self.genre = genre
        self.albums = albums

    def to_dict(self):
        artist_dict = {
            'id': self.id,
            'name': self.name,
            'genre': self.genre
        }
        if self.albums: 
            artist_dict['albums'] = self.albums

        return artist_dict
    
    def is_valid(self):
        if self.name and self.genre:
            return True
        else:
            return False
        
    def generate_errors(self):
        # errors = ""
        if not self.is_valid():
            errors = "Name can't be blank, Genre can't be blank"
        return errors
        

    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"
    
    # def __eq__(self, other):
    #     return self.__dict__ == other.__dict__
    
    def __eq__(self, other):
        if isinstance(other, Artist):
            return (self.id == other.id and
                    self.name == other.name and
                    self.genre == other.genre and
                    self.albums == other.albums)
        return False