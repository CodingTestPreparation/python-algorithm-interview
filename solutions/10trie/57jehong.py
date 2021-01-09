from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)   # {char: TrieNode} 이런식으로 저장됨
        self.wordIndex = -1
        self.palindromeIndex = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def isPalindrome(word: str) -> bool:
            return word == word[::-1]
        
    def insert(self, index, word) -> None:
        node = self.root
        revWord = word[::-1]
        for i, char in enumerate(revWord):
            if self.isPalindrome(word[0:len(word) - i]):        # 기존 단어의 시작부터 어디까지 palindrome인지
                node.palindromeIndex.append(index)              # 여태까지 palindrome이면 표시
            node = node.children[char]                          # {char: TrieNode}의 TrieNode를 새 node로
        node.wordIndex = index                                  # 해당 단어의 index 저장
        
    def search(self, index: int, word: str) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            # 판별로직3 탐색 중간에 wordIndex가 있고 word의 나머지가 palindrome인 경우
            if node.wordIndex >= 0:                             # word의 일부가 다른 단어의 끝
                if self.isPalindrome(word):                     # 다른 단어를 제외한 부분의 word가 palindrome
                    result.append([index, node.wordIndex])
            if not word[0] in node.children:
                return result
            
            # 단어 새로 세팅 예시
            # word = dcbb
            # word[0] = d, word = word[1:] = cbb
            # word[0] = c, word = word[1:] = bb
            node = node.children[word[0]]                       # 매번 다음 글자로 넘어간다
            word = word[1:]                                     # 매번 다음 글자 후부터 새로운 단어로 인식

        # 판별로직1 끝까지 탐색했을 때 w가 있는 경우(트라이에 revword가 있는 경우)
        if node.wordIndex >= 0 and node.wordIndex != index: 
            result.append([index, node.wordIndex])              # word + revword는 palindrome

        # 판별로직2 끝까지 탐색했을 때 p가 있는 경우
        for palindromeIndex in node.palindromeIndex:            # word를 탐색하다 palindromeIndex 발견
            result.append([index, palindromeIndex])             # word + revword의 word

        return result
    
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))        # result와 extend내의 리스트를 합친다

        return results
