"""
The bridge pattern is a design pattern used in software engineering that is meant to "decouple an abstraction from
its implementation so that the two can vary independently". In this example the abstraction is a document. There
are various document types, each represented as a subclass (Letter, Article, WikiPage) of the Document class.
The Document class uses the implementor class Renderer for rendering. The Renderer class has various
subclasses (Web, Paper, Audio) as well. Each can be used for rendering the document into the target format of the
corresponding renderer implementation.
According to Christopher Okhravi the pattern is called "bridge" because the UML looks like a bridge
"""

import unittest
from hamcrest import equal_to, assert_that
from patterns.structural.bridge.abstraction import Letter, WikiPage, Article
from patterns.structural.bridge.implementor import Paper, Audio, Web


class TestClient(unittest.TestCase):

    def test_letter_paper(self):
        document = Letter()
        document.set_renderer(Paper())
        assert_that(document.create(), equal_to("This is a letter # on paper"))

    def test_article_web(self):
        document = Article()
        document.set_renderer(Web())
        assert_that(document.create(), equal_to("This is an article # in html"))

    def test_wiki_audio(self):
        document = WikiPage()
        document.set_renderer(Audio())
        assert_that(document.create(), equal_to("This is a wiki page # in audio"))
