class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        profit = 0
        for price in prices:
            profit = max(price - min_price, profit)
            min_price = min(price, min_price)
        print("profit is ",profit)
        return profit
