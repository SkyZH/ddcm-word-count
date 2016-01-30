import unittest

import wordcount

from . import const

class FetcherTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fetcher = wordcount.Fetcher(const.url)

    def test_fetch(self):
        self.fetcher.fetch()
        self.assertIsNotNone(self.fetcher.response)
        self.assertIsNotNone(self.fetcher.data)
