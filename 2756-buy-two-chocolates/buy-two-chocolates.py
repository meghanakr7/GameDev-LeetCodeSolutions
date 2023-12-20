class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        firstSmallest = math.inf
        secSmallest = math.inf
        findex = -1
        for i in range(len(prices)):
            if prices[i] < firstSmallest:
                findex = i
                secSmallest = firstSmallest
                firstSmallest = prices[i] 
            if prices[i] < secSmallest and secSmallest >= firstSmallest and i!=findex:
                secSmallest = prices[i]
        if money - (firstSmallest + secSmallest) >= 0:
            return money - (firstSmallest + secSmallest)
        return money

        