class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        firstSmallest = math.inf
        secSmallest = math.inf
        findex = -1
        for i in range(len(prices)):
            print('price i is ',prices[i])
            if prices[i] < firstSmallest:
                findex = i
                secSmallest = firstSmallest
                firstSmallest = prices[i]
                
            if prices[i] < secSmallest and secSmallest >= firstSmallest and i!=findex:
                secSmallest = prices[i]
            print('after loop first and sec are ',firstSmallest, secSmallest)
        print('first and sec ',firstSmallest, secSmallest)
        if money - (firstSmallest + secSmallest) >= 0:
            return money - (firstSmallest + secSmallest)
        else:
            return money

        