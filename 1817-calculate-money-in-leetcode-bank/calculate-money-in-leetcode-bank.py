class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        print('number of weeks is ',weeks)
        count = 0
        money = 0
        while weeks:
            money += 7*(count) + 7*(8)//2
            weeks -= 1
            count += 1
        print('money is ',money, count)
        days = n % 7
        
        money += count*(days) + days*(days + 1)//2
        print('now money is ',money)
        return money

        