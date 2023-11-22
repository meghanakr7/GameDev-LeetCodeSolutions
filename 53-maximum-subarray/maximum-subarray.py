class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        currentSum = 0
        maxi = -math.inf
        while j < len(nums):
            if (currentSum < 0 and nums[j] >= currentSum):
                i = j
                currentSum = 0
            currentSum += nums[j]
            maxi = max(maxi, currentSum)
            j += 1
        return maxi
        