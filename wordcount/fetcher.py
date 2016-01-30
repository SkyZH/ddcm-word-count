import requests

class Fetcher(object):
    def __init__(self, url):
        self.url = url
        self.response = None
        self.data = None

    def fetch(self):
        self.response = requests.get(self.url)
        self.data = self.response.text
        return self.data
