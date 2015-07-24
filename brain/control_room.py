"""
Controller module
"""

import webbrowser
import os

from outfit.template_index import TemplateIndex
from outfit.template_nav_bar import TemplateNavBar
from outfit.template_banner import TemplateBanner
from outfit.template_footer import TemplateFooter
from outfit.template_tile import TemplateTile

class ControlRoom(object):
    """ Main controller class """

    def __init__(self, arg):
        super(ControlRoom, self).__init__()
        self.arg = arg

    @classmethod
    def generate_index_page(cls, movies, output_fp, options=None):
        """ Generates index.html """

        tiles = []
        genres = []
        for mov in movies:
            tiles.append(TemplateTile(mov))
            genres.extend(mov.genres)

        nav_bar = TemplateNavBar(sorted(set(genres)))
        banner = TemplateBanner()
        footer = TemplateFooter()
        index = TemplateIndex(
            movies=tiles,
            nav_bar=nav_bar,
            banner=banner,
            footer=footer,
            options=options)
        output_fp.write(index.html())

    @classmethod
    def launch_page(cls, page_fp):
        """ Launches fp on default browswer """
        # open the output file in the browser
        url = os.path.abspath(page_fp.name)
        webbrowser.open('file://' + url, new=2) # open in a new tab, if possible

