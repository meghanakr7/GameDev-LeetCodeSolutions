class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        count = 0
        money = 0
        while weeks:
            money += 7*(count) + 7*(8)//2
            weeks -= 1
            count += 1
        days = n % 7
        money += count*(days) + days*(days + 1)//2
        return money

        