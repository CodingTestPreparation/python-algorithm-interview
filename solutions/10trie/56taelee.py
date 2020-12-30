# version 1 : simple
# class TrieNode:
#
#     def __init__(self):
#         self.word = False
#         self.children = {}
#
# class Trie:
#
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word: str) -> None:
#         node = self.root
#         for char in word:
#             if not char in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.word = True
#
#
#     def search(self, word: str) -> bool:
#         node = self.root
#         for char in word:
#             if not char in node.children:
#                 return False
#             node = node.children[char]
#         return node.word
#
#     def startsWith(self, prefix: str) -> bool:
#         node = self.root
#         for char in prefix:
#             if not char in node.children:
#                 return False
#             node = node.children[char]
#         return True

# version 2 : using defaultdict(거의 version1과 큰 차이 없음)

from _collections import defaultdict
class TrieNode:

    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True


    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if not char in node.children:
                return False
            node = node.children[char]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if not char in node.children:
                return False
            node = node.children[char]
        return True

# Your Trie object will be instantiated and called as such:
word = "apple"
obj = Trie()
obj.insert(word)
print(obj.root.children)
# param_2 = obj.search(word)
# print(param_2)
# print(obj.search("app"))
# param_3 = obj.startsWith(prefix)