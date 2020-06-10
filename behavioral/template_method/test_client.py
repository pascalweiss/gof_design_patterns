"""
- Pattern Name -
Template Method

- Intent -
"Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets
subclasses redefine certain steps of an algorithm without changing the algorithm's structure." (GoF - Design Patterns)

- Additional Notes -
- It is similar to the strategy pattern. The only difference is, that the template method provides a skeleton of the
algorithm
- The pattern is highly related to the Open Closed Principle, which states that classes should be open for extension,
put closed for modification.
"""

import unittest
from patterns.behavioral.template_method.template_method import MongoCleaner, MySQLCleaner


class TestClient(unittest.TestCase):
    def test_mongo(self):
        cleaner = MongoCleaner()
        assert(cleaner.clean())

    def test_neo4j(self):
        cleaner = MySQLCleaner()
        assert(cleaner.clean())
