class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-10001] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        print('dp is ',dp)
        print('max is ',max(dp))
        return max(dp)
        