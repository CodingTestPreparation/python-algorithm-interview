from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        stock = -1
        for i in range(len(prices)):
            if i < len(prices) - 1 and prices[i] < prices[i + 1] and stock == -1:
                print('buy', prices[i])
                stock = prices[i]
            elif stock != -1 and (i == len(prices) - 1 or prices[i] > prices[i + 1]):
                print('sell', prices[i])
                sum += prices[i] - stock
                stock = -1
        return sum




a = [7,1,5,3,6,4]
b = [2,1,2,0,1]

solution = Solution()
a = solution.maxProfit(b)
print(a)
