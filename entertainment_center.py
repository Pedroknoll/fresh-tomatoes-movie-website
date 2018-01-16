"""Create instances/objects from the class Movie() """

import media
import fresh_tomatoes

# Add movies from The Movie Database by looking up ID's
# (for more details access README)
schindlers_list = media.Movie(424)
whiplash = media.Movie(244786)
dead_poets_society = media.Movie(207)
the_shinning = media.Movie(694)
oldboy = media.Movie(670)
lion = media.Movie(334543)

movies = [schindlers_list, whiplash, dead_poets_society, the_shinning,
          oldboy, lion]

# Generate html website
fresh_tomatoes.open_movies_page(movies)
