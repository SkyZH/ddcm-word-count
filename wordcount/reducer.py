class Reducer(object):
    def __init__(self):
        pass
    def word_counter(self, word_list, origin_list):
        for word, count in origin_list.items():
            if word in word_list:
                word_list[word] += count
            else:
                word_list[word] = count
    def do_reduce(self, dataA, dataB):
        data = {}
        data["done"] = list(set(dataA["done"] + dataB["done"]))
        data["to"] = [
            i for i in set(dataA["to"] + dataB["to"]) if not(i in data["done"])
        ]
        word_list = {}
        self.word_counter(word_list, dataA["words"])
        self.word_counter(word_list, dataB["words"])
        data["words"] = word_list
        return data
