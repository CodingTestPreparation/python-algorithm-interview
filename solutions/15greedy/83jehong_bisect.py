import bisect

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        count = 0
        
        for size in s:
            i = bisect.bisect_right(g, size)
            if i > count:
                count += 1
    
        return count