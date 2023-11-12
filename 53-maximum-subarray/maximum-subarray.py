class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestSum = 0
        n = len(nums)
        dp = [-math.inf]*(n+1)
        for i in range(len(nums)):
            dp[i] = nums[i]
        tillMax = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)
        
        