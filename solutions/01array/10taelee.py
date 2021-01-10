from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum


a = [1,4,3,2]
solution = Solution()
print(solution.arrayPairSum(a))
