"""
Template for tile.html
"""

from templates import HtmlTemplates

class TemplateTile(HtmlTemplates):
    """ Represents a movie tile template """

    def __init__(self, movie):
        self._name = "tile"
        self.movie = movie

    def html(self):
        """ Returns the generated HTML from the template"""
        return HtmlTemplates.get(self._name).format(
            movieid=self.movie.movie_id,
            poster=self.movie.poster,
            title=self.movie.title,
            rating=self.movie.rating,
            year=self.movie.year,
            plot=self.movie.plot)
