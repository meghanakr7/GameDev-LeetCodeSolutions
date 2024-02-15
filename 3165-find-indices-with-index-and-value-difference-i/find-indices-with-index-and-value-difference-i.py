class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        res = []
        for i in range(len(nums) - indexDifference):
            for j in range(i+indexDifference, len(nums)):
                if(abs(nums[i] - nums[j]) >= valueDifference):        
                    res.append(i)
                    res.append(j)
        if(not res):
            return [-1,-1]
        return res