"""
Template for index.html
"""

import json
from templates import HtmlTemplates

class TemplateIndex(HtmlTemplates):
    """ Represents the index page """

    def __init__(self, movies=None, nav_bar=None, banner=None, footer=None, options=None):
        """
        @Params:
            movies - array of HtmlTemplates objects. Collection of movie TemplateTiles.
            nav_bar - TemplplateNavBar. Navigation bar.
            banner - TemplateBanner. Banner ad.
            footer - TemplateFooter. Footer of the page.
            options - Dictionary of options
        """
        self._name = "index"

        opts = options or {}
        self.root_view_path = opts["root_view_path"] \
            if "root_view_path" in opts else ""

        self.nav_bar = nav_bar
        self.banner = banner
        self.movies = movies or []
        self.footer = footer

    def html(self):
        """ Returns the generated HTML from the template"""
        movie_ids = {}
        movie_tiles = []
        for mov in self.movies:
            movie_tiles.append(mov.html())
            movie_ids[mov.movie.movie_id] = mov.movie.__dict__

        return HtmlTemplates.get(self._name).format(
            root_view_path=self.root_view_path,
            movie_ids=json.dumps(movie_ids),
            nav_bar=(self.nav_bar.html() if self.nav_bar else ""),
            banner=(self.banner.html() if self.banner else ""),
            footer=(self.footer.html() if self.footer else ""),
            tiles=("".join(movie_tiles))
            )
