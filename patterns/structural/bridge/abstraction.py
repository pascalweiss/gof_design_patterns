# ------------------- Abstraction --------------------
from patterns.structural.bridge.implementor import Renderer


class Document:
    _renderer = None
    def set_renderer(self, renderer: Renderer):
        self._renderer = renderer

    def create(self):
        raise NotImplementedError


# ------------------ Refined Abstraction --------------

class Letter(Document):
    def create(self):
        return self._renderer.render("This is a letter")


class WikiPage(Document):
    def create(self):
        return self._renderer.render("This is a wiki page")


class Article(Document):
    def create(self):
        return self._renderer.render("This is an article")
