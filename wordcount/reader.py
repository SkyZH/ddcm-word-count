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

    def parse(self):
        self.parser.feed(self.data)
        return iter(self.parser.data)
