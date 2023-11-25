class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        totalSum = sum(nums)
        prevSum = 0
        for i in range(len(nums)):
            res[i] = abs(totalSum - nums[i]*(n-i)) + (nums[i] *i - prevSum)
            totalSum -=nums[i]
            prevSum += nums[i]
        return res