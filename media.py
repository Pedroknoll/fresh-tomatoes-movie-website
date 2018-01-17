""" Define Movie class and its atributtes
    The attributes:
      title: the title of the movies
      storyline: the storyline of the movie
      vote_average: the average 0-10 of the movie
      trailer: the url with the video of the movie's trailer
      poster: the url with an image of the movie's poster
      release_year: the release year of the movie"""

from os import getenv
from datetime import datetime
from urllib.parse import urljoin
from webbrowser import open

from tmdbv3api import TMDb
# Change the imported class name to avoid conflicts
from tmdbv3api import Movie as theMovie

# initialize a TMDb object
tmdb = TMDb()

# Get the API Key saved as an environment variable.
tmdb.api_key = getenv('TMDB_API_KEY')

# initialize a theMovie object
movie = theMovie()


# Movie class that takes TMDB movie ID to initialize, and fills in attributes
class Movie():
    def __init__(self, movie_id):
        self.title = movie.details(movie_id).title
        self.storyline = movie.details(movie_id).overview
        self.vote_average = movie.details(movie_id).vote_average

        # Convert a relative video url to an absolute url from the first video
        # on the movie's list
        self.trailer = urljoin("https://www.youtube.com", "/watch?v=" +
                               movie.videos(movie_id)[0].key)

        # Convert a relative poster url to an absolute url
        self.poster = urljoin("https://image.tmdb.org", "/t/p/original"
                              + movie.details(movie_id).poster_path)

        # convert a string datetime to datetime
        self.release_year = datetime.strptime(
                                     movie.details(movie_id).release_date,
                                     "%Y-%m-%d").year

    # Open the youtube trailer url
    def show_trailer(self):
        open(self.trailer)
