from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.nextChars = defaultdict(TrieNode)

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.nextChars[char]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.nextChars:
                return False
            node = node.nextChars[char]

        return True if node.endOfWord == True else False        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.nextChars:
                return False
            node = node.nextChars[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)