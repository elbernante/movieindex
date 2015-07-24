"""
Entry point to launch My Movies
"""

import os

from brain.control_room import ControlRoom
from soul.movie import Movie

ML_VIEW_PATH = "outfit/"
ML_INDEX_FILE = os.path.dirname(os.path.abspath(__file__)) + "/index.html"

def main():
    """ Generates index.html file and luaches the file in the default browser """

    options = {"root_view_path": ML_VIEW_PATH}

    # Retrieve saved movies
    movies = Movie.get_movies()

    # Generate index.html file
    index_file = open(ML_INDEX_FILE, "w")
    ControlRoom.generate_index_page(movies, index_file, options)
    index_file.close()

    # Lauch generated index.html file in default browser
    ControlRoom.launch_page(index_file)

if __name__ == '__main__':
    main()
