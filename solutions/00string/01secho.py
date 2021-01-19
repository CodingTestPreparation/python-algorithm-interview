from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
      plainStr = []
      index = 0
      s = s.lower()
      for v in list(s):
        if(v.isalnum()): plainStr.append(v)
      if (len(plainStr) % 2 != 0): index = 1
      if(len(plainStr) < 2): return True
      begin = plainStr[0:int(len(plainStr) / 2)]
      end = plainStr[int(len(plainStr) / 2) + index:]
      end.reverse()
      for v in range(len(begin)):
        if (begin[v] != end[v]): return False
      return True
    isPalindrome("","0P")
      