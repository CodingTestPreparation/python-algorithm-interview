from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftProduct = [1] * len(nums)
        rightProduct = [1] * len(nums)
        for i in range(1, len(nums)):
            leftProduct[i] = nums[i - 1] * leftProduct[i - 1]
        for j in range(len(nums) - 2, -1, -1):
            rightProduct[j] = rightProduct[j + 1] * nums[j + 1]
        return [leftProduct[i] * rightProduct[i] for i in range(len(nums)) ]


solution = Solution()
a = solution.productExceptSelf([1, 2, 3, 4])
print(a)


