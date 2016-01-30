import unittest

import wordcount

from . import const

class ReaderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fp = open(const.html_path, "rt")
        cls.reader = wordcount.Reader(fp.read())
        fp.close()

    def test_read(self):
        for sentence in self.reader.parse():
            for word in sentence:
                self.assertNotIn(' ', word)
