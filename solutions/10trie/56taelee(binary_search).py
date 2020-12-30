from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

class Trie:
    def __init__(self):
        self.dict = {}

    def insert(self, word: str) -> None:
        if not len(word) in self.dict:
            self.dict[len(word)] = []
        self.dict[len(word)].append(word)

    def search(self, word: str) -> bool:
        if not len(word) in self.dict:
            return False
        self.dict[len(word)].sort()
        if count_by_range(self.dict[len(word)], word, word) != 0:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for key in self.dict:
            if len(prefix) > key:
                continue
            start_str = prefix + "a" * (key - len(prefix))
            end_str = prefix + "z" * (key - len(prefix))
            self.dict[key].sort()
            if count_by_range(self.dict[key],start_str, end_str) > 0:
                return True
        return False

# Test code
obj = Trie()
obj.insert("app")
obj.insert("apple")
obj.insert("beer")
obj.insert("add")
obj.insert("jam")
obj.insert("rental")
obj.search("apps")
print(obj.search("app"))
