"""
- Pattern Name -
Proxy

- Intent -
"Provide a surrogate or placeholder for another object to control access to it." (GoF - Design Patterns)

- Also Known As -
Surrogate
"""

import unittest
from hamcrest import equal_to, assert_that

from patterns.structural.proxy.test_utils.domain import Data
from patterns.structural.proxy.test_utils.subject_factory import create_submitter


class TestClient(unittest.TestCase):
    def test(self):
        secret = Data("Sensitive data")
        submitter = create_submitter()
        response = submitter.submit(secret)
        assert_that(response, equal_to("received encrypted data"))
