from bisect import bisect_left, bisect_right

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        
        if left == right:
            return -1
    
        return left