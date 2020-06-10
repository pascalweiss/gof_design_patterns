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

