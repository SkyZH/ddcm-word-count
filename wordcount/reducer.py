class Reducer(object):
    def __init__(self):
        pass
    def do_reduce(dataA, dataB):
        data = {}
        data["done"] = list(set(dataA["done"] + dataB["done"]))
        data["to"] = [
            i for i in set(dataA["to"] + dataB["to"]) if not(i in data["done"])
        ]
        data["words"] = {}
        with data["words"] as word_list:
            for word, count in dataA["words"].items() + dataB["words"].items():
                if word in word_list:
                    word_list[word] += count
                else:
                    word_list[word] = count
        return data
