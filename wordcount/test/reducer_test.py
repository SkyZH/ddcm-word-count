import unittest

import wordcount

from . import const

class ReducerTest(unittest.TestCase):
    def test_reducer_url_done(self):
        reducer = wordcount.Reducer()
        dataA = {
            "done": [
                "https://skyzh.github.io/social-network-site/1.html",
                "https://skyzh.github.io/social-network-site/2.html",
                "https://skyzh.github.io/social-network-site/3.html",
                "https://skyzh.github.io/social-network-site/4.html"
            ],
            "to": [],
            "words": {
            }
        }
        dataB = {
            "done": [
                "https://skyzh.github.io/social-network-site/5.html",
                "https://skyzh.github.io/social-network-site/6.html",
                "https://skyzh.github.io/social-network-site/7.html"
            ],
            "to": [],
            "words": {
            }
        }
        data = reducer.do_reduce(dataA, dataB)
        self.assertEqual(sorted(data["done"]), sorted([
                "https://skyzh.github.io/social-network-site/1.html",
                "https://skyzh.github.io/social-network-site/2.html",
                "https://skyzh.github.io/social-network-site/3.html",
                "https://skyzh.github.io/social-network-site/4.html",                "https://skyzh.github.io/social-network-site/5.html",
                "https://skyzh.github.io/social-network-site/6.html",
                "https://skyzh.github.io/social-network-site/7.html"
        ]))
    def test_reducer_url_to(self):
        reducer = wordcount.Reducer()
        dataA = {
            "to": [
                "https://skyzh.github.io/social-network-site/1.html",
                "https://skyzh.github.io/social-network-site/2.html",
                "https://skyzh.github.io/social-network-site/3.html",
                "https://skyzh.github.io/social-network-site/4.html"
            ],
            "done": [],
            "words": {
            }
        }
        dataB = {
            "to": [
                "https://skyzh.github.io/social-network-site/5.html",
                "https://skyzh.github.io/social-network-site/6.html",
                "https://skyzh.github.io/social-network-site/7.html"
            ],
            "done": [],
            "words": {
            }
        }
        data = reducer.do_reduce(dataA, dataB)
        self.assertEqual(sorted(data["to"]), sorted([
                "https://skyzh.github.io/social-network-site/1.html",
                "https://skyzh.github.io/social-network-site/2.html",
                "https://skyzh.github.io/social-network-site/3.html",
                "https://skyzh.github.io/social-network-site/4.html",                "https://skyzh.github.io/social-network-site/5.html",
                "https://skyzh.github.io/social-network-site/6.html",
                "https://skyzh.github.io/social-network-site/7.html"
        ]))
    def test_reducer_url_to_except(self):
        reducer = wordcount.Reducer()
        dataA = {
            "to": [
                "https://skyzh.github.io/social-network-site/1.html",
                "https://skyzh.github.io/social-network-site/2.html",
                "https://skyzh.github.io/social-network-site/3.html",
                "https://skyzh.github.io/social-network-site/4.html"
            ],
            "done": [
                "https://skyzh.github.io/social-network-site/1.html",
                "https://skyzh.github.io/social-network-site/5.html"
            ],
            "words": {
            }
        }
        dataB = {
            "to": [
                "https://skyzh.github.io/social-network-site/5.html",
                "https://skyzh.github.io/social-network-site/6.html",
                "https://skyzh.github.io/social-network-site/7.html"
            ],
            "done": [
                "https://skyzh.github.io/social-network-site/2.html",
                "https://skyzh.github.io/social-network-site/6.html"
            ],
            "words": {
            }
        }
        data = reducer.do_reduce(dataA, dataB)
        self.assertEqual(sorted(data["to"]), sorted([
                "https://skyzh.github.io/social-network-site/3.html",
                "https://skyzh.github.io/social-network-site/4.html",                                              "https://skyzh.github.io/social-network-site/7.html"
        ]))
        self.assertEqual(sorted(data["done"]), sorted([
                "https://skyzh.github.io/social-network-site/1.html",
                "https://skyzh.github.io/social-network-site/5.html",
                "https://skyzh.github.io/social-network-site/2.html",
                "https://skyzh.github.io/social-network-site/6.html"
        ]))
    def test_reducer_word(self):
        reducer = wordcount.Reducer()
        dataA = {
            "to": [],
            "done": [],
            "words": {
                "apple": 2,
                "orange": 3
            }
        }
        dataB = {
            "to": [],
            "done": [],
            "words": {
                "apple": 5,
                "link": 1
            }
        }
        data = reducer.do_reduce(dataA, dataB)
        self.assertEqual(data["words"]["apple"], 7)
        self.assertEqual(data["words"]["orange"], 3)
        self.assertEqual(data["words"]["link"], 1)
