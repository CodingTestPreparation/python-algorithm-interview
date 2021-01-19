from typing import List
from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
              sum = nums[i] + nums[left] + nums[right]
              if sum < 0:
                  left += 1
              if sum > 0:
                  right -= 1
              else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left + 1] == nums[left]:
                    left += 1
                while left < right and nums[right - 1] == nums[right]:
                    right -= 1
                left += 1
                right -= 1
        return result
