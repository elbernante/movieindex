"""
Module for Movie class
"""

import webbrowser
import os
import json

class Movie(object):
    """ Represents a Movie object """

    _MOVIE_LIST_FILE = "movie_list.json"
    _MOVIE_LIST_PATH = os.path.dirname(os.path.abspath(__file__)) + "/"

    def __init__(
            self,
            title,
            poster,
            trailer,
            year="",
            release_date="",
            genres=None,
            actors=None,
            rating="",
            directors=None,
            writers=None,
            plot="",
            synopsis="",
            movie_id=""
        ):
        super(Movie, self).__init__()
        self.title = title
        self.poster = poster
        self.trailer = trailer
        self.year = year
        self.release_date = release_date
        self.genres = genres or []
        self.actors = actors or []
        self.rating = rating
        self.directors = directors or []
        self.writers = writers or []
        self.plot = plot
        self.synopsis = synopsis
        self.movie_id = movie_id

    def play_trailer(self):
        """ Plays the trailer of the movie in default browser """
        webbrowser.open(self.trailer, new=2)

    @classmethod
    def movie_from_json(cls, mov_json):
        """ Returns an instance of Movie object from a JSON object that represents a movie """
        return cls(
            mov_json["Title"],
            mov_json["Poster"],
            mov_json["Trailer"],
            mov_json["Year"],
            mov_json["Released"],
            mov_json["Genre"].split(", "),
            mov_json["Actors"].split(", "),
            mov_json["imdbRating"],
            mov_json["Director"].split(", "),
            mov_json["Writer"].split(", "),
            mov_json["Plot"],
            mov_json["Synopsis"],
            mov_json["imdbID"])

    @classmethod
    def get_movies(cls):
        """ Returns instances of Movie from a list of movies in a JSON file """
        data_source = open(cls._MOVIE_LIST_PATH + cls._MOVIE_LIST_FILE, "r")
        data_content = data_source.read()
        json_object = json.loads(data_content)
        data_source.close()

        movies = []
        for mov in json_object:
            movies.append(cls.movie_from_json(mov))
        return movies
