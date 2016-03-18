import unittest
import aiohttp

import wordcount

from . import const

class FetcherTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        session = aiohttp.ClientSession(loop = loop)
        cls.fetcher = wordcount.Fetcher(session, const.url)

    @unittest.skipIf(const.devel, "Development Environment")
    def test_fetch(self):
        self.fetcher.fetch()
        self.assertIsNotNone(self.fetcher.response)
        self.assertIsNotNone(self.fetcher.data)
