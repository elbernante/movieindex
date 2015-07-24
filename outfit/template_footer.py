"""
Template for footer.html
"""

from templates import HtmlTemplates

class TemplateFooter(HtmlTemplates):
    """ Represents the page footer """

    def __init__(self):
        self._name = "footer"

    def html(self):
        """ Returns the generated HTML from the template"""
        return HtmlTemplates.get(self._name)
