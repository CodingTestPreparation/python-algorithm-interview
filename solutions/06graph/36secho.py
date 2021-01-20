from typing import List
from itertools import combinations
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      combis = []
      result = []
      for i in range(1, len(candidates)+1):
        combis.append(list(map(list, combinations(candidates, i))))
      for i in range(len(combis)):
        for j in range(len(combis[i])):
          if ((target % sum(combis[i][j])) == 0):
            print(combis[i][j])
    combinationSum("",[2,3,6,7],7)
