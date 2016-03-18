import unittest
import aiohttp

import wordcount

from . import const

class FetcherTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        session = aiohttp.ClientSession()
        cls.fetcher = wordcount.Fetcher(session, const.url)

    @unittest.skipIf(const.devel, "Development Environment")
    def test_fetch(self):
        self.assertIsNotNone(self.fetcher.fetch())
