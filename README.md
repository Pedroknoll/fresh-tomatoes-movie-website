## Fresh Tomatoes - Movie Trailer Website
Movie trailer website is a simple project create to the Udacity Fullstack Nanodegree.
The website lists some movies with basic information and their trailers.

### Pre-requisites
- Git installed
- Python installed (Python 3 recommended)
- tmdbv3api

### Install
1. Clone, or fork and clone, the repository:
`git clone https://github.com/Pedroknoll/fresh-tomatoes-movie-website.git`

2. Install tmdbv3api available on the Python Package Index (PyPI) at [tmdbv3api](https://pypi.python.org/pypi/tmdbv3api).
Using the command `pip install -r requirements.txt`

3. Set an environment variable called TMDB_API_KEY containing your unique API key (from your account on the [The Movie Database](https://www.themoviedb.org/)). This step is mandatory for you access the TMDB API.

3. You can edit the file entertainment_center.py to add, remove or change the movie you want to display. You will have to manually look up the movies ID's.
For that, access the movie's page at the The Movie Database. The ID is the number after the last slash at the movie's URL.

4. Access the entertainment_center.py and run it at the terminal:`python entertainment_center.py`

### License
This project is licensed under the terms of the [MIT license](https://github.com/Pedroknoll/movie-trailer-website/blob/master/LICENSE).
