"""
Module for generating HTML pages from templates
"""
from abc import ABCMeta, abstractmethod
import os

class HtmlTemplates(object):
    """ Abstract class for HTML template classes.
        Factory class for functions for reading the contents of templates from file and caches it.
        """

    __metaclass__ = ABCMeta

    _TEMPLATE_FILE_PATTERN = "template_%s.html"
    _TEMPLATE_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__)) + "/"

    _cached_templates = {}

    _name = ""

    @abstractmethod
    def html(self):
        """ Returns the generated HTML from the template. Sublcasses should override this. """
        return HtmlTemplates.get(self._name)

    @classmethod
    def get(cls, name):
        """ Returns the specified template """
        if not name in cls._cached_templates:
            cls._cached_templates[name] = cls._read_template_from_file(name)
        return cls._cached_templates[name]

    @classmethod
    def clean_cache(cls):
        """ Deletes all cached template """
        cls._cached_templates = {}

    @classmethod
    def set_folder_path(cls, path):
        """ Sets the folder path where the templates are stored """
        cls._TEMPLATE_FOLDER_PATH = path

    @classmethod
    def _read_template_from_file(cls, name):
        """ Reads the contents of template file """
        data_source = open(cls._TEMPLATE_FOLDER_PATH + (cls._TEMPLATE_FILE_PATTERN % name), "r")
        data_content = data_source.read()
        data_source.close()
        return data_content
