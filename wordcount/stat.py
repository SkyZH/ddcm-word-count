class Stat(object):
    def __init__(self, parser):
        self.parser = parser

    def stat(self):
        word_list = {}
        for sentence in self.parser:
            for word in sentence:
                if word in word_list:
                    word_list[word] += 1
                else:
                    word_list[word] = 1
        return word_list
