class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        s = set()
        count = len(nums)
        res = []
        while count:
            s = set()
            for i in range(len(nums)):
                s.add(nums[i])
            print('s is ',s)
            for i in list(s):
                nums.remove(i)
            res.append(list(s))
            print('nums is ',nums)
            count = len(nums)
        print('res is ',res)
        return res
        

            
        