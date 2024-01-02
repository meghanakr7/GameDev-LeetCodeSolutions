class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        prevRes = 0
        for i in range(len(nums)):
            res.append(prevRes + nums[i])
            prevRes += nums[i]
        print('res is ',res)
        return res