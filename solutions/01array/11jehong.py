class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prev = 1
        for i in range(len(nums)):
            result[i] *= prev
            prev *= nums[i]
        
        prev = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= prev
            prev *= nums[i]
        
        return result
            