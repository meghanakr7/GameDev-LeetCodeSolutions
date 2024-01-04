class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minReq = nums[0]
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            minReq = min(minReq ,total)
        if(minReq < 0):
            minReq = abs(minReq) + 1
            return minReq
        return 1