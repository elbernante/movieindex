"""
Template for nav_bar.html
"""

from templates import HtmlTemplates

class TemplateNavBar(HtmlTemplates):
    """ Represents the page navigation bar """

    _LIST_ITEM_TEMPLATE = '''
        <li value=\"{value}\" data-role="select-entry">
            <a href=\"#\">{display_text}</a>
        </li>
        '''

    def __init__(self, filters=None):
        self._name = "nav_bar"
        self.filters = filters or []

    def html(self):
        """ Returns the generated HTML from the template"""
        genre_filters = (TemplateNavBar._LIST_ITEM_TEMPLATE.format(value=f, display_text=f) \
            for f in self.filters)
        return HtmlTemplates.get(self._name).format(
            genre_filters=("".join(genre_filters)))
