class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if(len(cost) == 1):
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        i = 2
        dp = [0]*(len(cost)+1)
        dp[0] = 0
        dp[1] = 0
        while i <= len(cost):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            i += 1
        return dp[n]
        


