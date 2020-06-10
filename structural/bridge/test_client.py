"""
- Pattern Name -
Bridge

- Intent -
"Decouple an abstraction from its implementation so that the two can vary independently." (GoF - Design Patterns)

- Also Known As -
Handle/Body

- Example Description -
In this example the abstraction is a document. There are various document types, each represented as a
subclass (Letter, Article, WikiPage) of the Document class. The Document class uses the implementor class
Renderer for rendering. The Renderer class has various subclasses (Web, Paper, Audio) as well. Each can
be used for rendering the document into the target format of the corresponding renderer implementation.
By applying the bridge pattern, any document can be combined with any renderer. Like in a cartesian product.
The abstraction interface and the implementor interface act as a bridge between concrete abstractions and
concrete implementors.
"""

import unittest
from hamcrest import equal_to, assert_that
from structural.bridge.abstraction import Letter, WikiPage, Article
from structural.bridge.implementor import Paper, Audio, Web


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

