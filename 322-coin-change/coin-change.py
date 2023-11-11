class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        dp = [n+1]*(n+1)
        dp[0] = 0
        for s in range(len(coins)):
            if coins[s] <= amount:
                dp[coins[s]] = 1
        for target in range(amount+1):
            for s in range(len(coins)):
                if target - coins[s] <=0:
                    continue
                else:
                    dp[target] = min(dp[target] , 1 + dp[target - coins[s]])
        if dp[amount] == n + 1:
            return -1
        return dp[amount]
            