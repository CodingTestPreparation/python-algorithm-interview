from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sum = 0
        s.sort()
        g.sort()
        print(g, s)

        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                sum += 1
                i += 1
            j += 1
        return sum

g = [10, 9, 8, 7]
s = [5,6,7,8]

solution = Solution()
print(solution.findContentChildren(g, s))