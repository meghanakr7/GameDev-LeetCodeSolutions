class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        prevRes = 0
        for i in range(len(nums)):
            prevRes += nums[i]
            res.append(prevRes)
            
        return res