class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        diff = 0
        nextSum = [0]*n
        totalSum = sum(nums)
        prevSum = 0
        for i in range(len(nums)):
            res[i] = abs(totalSum - nums[i]*(n-i)) + (nums[i] *i - prevSum)
            totalSum -=nums[i]
            prevSum += nums[i]
        #     print("total and prev sum ",res[i], totalSum, prevSum)
        # print("res is ",res)
        return res