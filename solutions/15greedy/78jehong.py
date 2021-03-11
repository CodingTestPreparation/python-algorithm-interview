class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        
        for sell in prices:
            if (sell < buy):
                buy = sell
            elif (sell > buy):
                profit += sell - buy
                buy = sell
        
        return profit