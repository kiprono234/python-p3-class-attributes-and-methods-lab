
class Song:
    all = []            
    count = 0           
    genres = []         
    artists = []       
    genre_count = {}    
    artist_count = {}   

    def __init__(self, name, artist=None, genre=None):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_all(self)      
        Song.add_song_to_count()        
        if genre:
            Song.add_to_genres(genre)   
            Song.add_to_genre_count(genre)  
        if artist:
            Song.add_to_artists(artist) 
            Song.add_to_artist_count(artist)  

    @classmethod
    def add_song_to_all(cls, song):
        cls.all.append(song)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def show_song_names(cls):
        print([song.name for song in cls.all])
    
    @classmethod
    def show_song_count(cls):
        print(f"Total number of songs: {cls.count}")

    @classmethod
    def show_genres(cls):
        print(f"Unique genres: {cls.genres}")

    @classmethod
    def show_artists(cls):
        print(f"Unique artists: {cls.artists}")

    @classmethod
    def show_genre_count(cls):
        print(f"Genre counts: {cls.genre_count}")

    @classmethod
    def show_artist_count(cls):
        print(f"Artist counts: {cls.artist_count}")
        pass