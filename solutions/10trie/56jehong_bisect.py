from bisect import bisect_left, bisect_right

class Trie:

    def __init__(self):
        self.trie = []

    def insert(self, word: str) -> None:
        if len(self.trie) < len(word) + 1:
            for _ in range(len(self.trie), len(word) + 1):
                self.trie.append([])

        self.trie[len(word)].append(word)

    def search(self, word: str) -> bool:
        if len(self.trie) < len(word) + 1:
            return False
        return word in self.trie[len(word)]

    def count(self, arr: list, left_value: str, right_value: str) -> int:
        right_index = bisect_right(arr, right_value)
        left_index = bisect_left(arr, left_value)

        return right_index - left_index

    def startsWith(self, prefix: str) -> bool:
        count = 0

        for i in range(len(prefix), len(self.trie)):
            self.trie[i].sort()
            right = prefix + (i - len(prefix)) * 'z'
            left = prefix + (i - len(prefix)) * 'a'
            count += self.count(self.trie[i], left, right)

            if count > 0:
                break

        return count > 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)