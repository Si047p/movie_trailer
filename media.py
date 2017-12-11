""" Defines media types with their attributes
"""

class Movie():
    """Class stores the information related to a movie.

    Attributes:
        movie_title: The movie's title.
        poster_image: URL to the movie's poster or box art.
        trailer_youtube: URL to the movie's trailer on YouTube
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Inits SampleClass with title, image url and trailer url""" 
        self.title = movie_title  #Assign title
        self.poster_image_url = poster_image  #Assign image url
        self.trailer_youtube_url = trailer_youtube #Assign trailer url
