import media
import fresh_tomatoes

""" Creates a fresh tomatoes HTML file with defined movie list.
"""

# Create a Movie class instance for each favorite movies.
top_gun = media.Movie("Top Gun",
                      "https://upload.wikimedia.org/wikipedia/en/4/46/"
                      +"Top_Gun_Movie.jpg",
                      "https://youtu.be/qAfbp3YX9F0")

get_out = media.Movie("Get Out(2017)",
                      "https://cdn.traileraddict.com/content/"+
                      "universal-pictures/get-out-2017-2.jpg",
                      "https://youtu.be/sRfnevzM9kQ")

star_wars = media.Movie("Star Wars: The Last Jedi",
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/"+
                        "Star_Wars_The_Last_Jedi.jpg",
                        "https://youtu.be/Q0CbN8sfihY")

godfather = media.Movie("Godfather", 
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/"+
                        "Godfather_ver1.jpg",
                        "https://youtu.be/dNE2PvbesQU")

marked_for_death = media.Movie("Marked For Death",
                               "https://upload.wikimedia.org/wikipedia/en/9/99/"
                               +"Marked_For_Death_film.jpg",
                               "https://youtu.be/9KvW9Q9875Q")

tears_of_the_sun = media.Movie("Tears Of The Sun",
                               "https://upload.wikimedia.org/wikipedia/en/d/d9/"
                               +"Tears_of_the_Sun_movie.jpg",
                               "https://youtu.be/DuTlpSfptO0")


# Create a list of movies
movies = [top_gun, get_out, star_wars, godfather, marked_for_death, tears_of_the_sun]


# Create a webpage from the movie list
fresh_tomatoes.open_movies_page(movies)
