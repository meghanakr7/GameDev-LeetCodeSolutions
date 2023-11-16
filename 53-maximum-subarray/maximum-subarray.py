class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax = [0] * len(nums)
        localMax[0] = nums[0]
        maxi = nums[0]
        for i in range(1, len(nums)):
            localMax[i] = max(nums[i], localMax[i-1] + nums[i])
        return max(localMax)

        