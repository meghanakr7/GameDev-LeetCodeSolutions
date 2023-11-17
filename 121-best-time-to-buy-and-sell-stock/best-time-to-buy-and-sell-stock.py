class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        n = len(prices)
        for price in prices[1:n]:
            profit = max(profit, price - min_price)
            min_price = min(min_price, price)
        print("profit ",profit)
        return profit