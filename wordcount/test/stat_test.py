import unittest

import wordcount

from . import const

class StatTest(unittest.TestCase):
    def test_stst(self):
        def word():
            return iter(["apple", "pie", "orange", "link"])
        def sentence():
            for i in range(3):
                yield word()
        stat = wordcount.Stat(sentence())
        result = stat.stat()
        self.assertEqual(result["apple"], 3)
        self.assertEqual(result["pie"], 3)
        self.assertEqual(result["orange"], 3)
        self.assertEqual(result["link"], 3)
