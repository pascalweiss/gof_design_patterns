import unittest
from behavioral.template_method.template_method import MongoCleaner, MySQLCleaner


class TestClient(unittest.TestCase):
    def test_mongo(self):
        cleaner = MongoCleaner()
        assert(cleaner.clean())

    def test_neo4j(self):
        cleaner = MySQLCleaner()
        assert(cleaner.clean())
