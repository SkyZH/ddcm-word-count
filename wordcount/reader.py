from html.parser import HTMLParser

class SocoalHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.isParaTag = False
        self.data = []

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.isParaTag = True
    def handle_endtag(self, tag):
        if tag == "p":
            self.isParaTag = False
    def handle_data(self, data):
        self.data.append(data)

class Reader(object):
    def __init__(self, data):
        self.parser = SocoalHTMLParser()
        self.data = data

    def word(self, data):
        return iter(data.split(' '))

    def sentence(self, data):
        for sentence in iter(data):
            yield self.word(sentence)

    def parse(self):
        self.parser.feed(self.data)
        return self.sentence(self.parser.data)
