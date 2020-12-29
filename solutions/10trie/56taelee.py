from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# a = ["ab", "aa", "az", "ad"]
# a.sort()
# print(count_by_range(a, "ab", "ac"))

class Trie:
    def __init__(self):
        self.dict = {}
        """
        Initialize your data structure here.
        """

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
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
        """
        Returns if the word is in the trie.
        """

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

        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

# Your Trie object will be instantiated and called as such:
# word = "apple"
obj = Trie()
obj.insert("app")
obj.insert("apple")
obj.insert("beer")
obj.insert("add")
obj.insert("jam")
obj.insert("rental")
obj.search("apps")
print(obj.dict[3])
print(obj.search("app"))
# print(obj.hi)
# obj.insert(word)
# param_2 = obj.search(word)
# print(obj.search("appl"))
# print(obj.startsWith("appled"))
# param_3 = obj.startsWith("app")
