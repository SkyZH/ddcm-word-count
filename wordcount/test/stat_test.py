import unittest

import wordcount

from . import const

class StatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.stat = wordcount.Stat()
