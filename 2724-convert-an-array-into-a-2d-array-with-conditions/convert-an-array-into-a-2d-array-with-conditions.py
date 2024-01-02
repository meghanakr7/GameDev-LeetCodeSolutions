class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = len(nums)
        res = []
        while count:
            s = set()
            for i in range(len(nums)):
                s.add(nums[i])
            for i in list(s):
                nums.remove(i)
            res.append(list(s))
            count = len(nums)
        return res
        

            
        