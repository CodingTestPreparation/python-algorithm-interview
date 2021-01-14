class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        minPrice = 10001
        profit = 0
        maxProfit = 0
        for i in range(len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
            if prices[i] > minPrice:
                profit = prices[i] - minPrice
            if profit >= maxProfit:
                maxProfit = profit
        
        return maxProfit