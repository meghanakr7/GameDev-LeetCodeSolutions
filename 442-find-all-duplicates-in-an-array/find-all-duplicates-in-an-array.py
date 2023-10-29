class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            ind = abs(nums[i])-1
            if nums[ind] < 0:
                res.append(ind+1)
            else:
                nums[ind] = -nums[ind]
        return res