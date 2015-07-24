"""
Template for banner.html
"""

from templates import HtmlTemplates

class TemplateBanner(HtmlTemplates):
    """ Represents the banner in the page"""

    def __init__(self):
        self._name = "banner"

    def html(self):
        """ Returns the generated HTML from the template"""
        return HtmlTemplates.get(self._name)
