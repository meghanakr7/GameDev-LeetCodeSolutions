class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        res1 = []
        def dfs(cur):
            if len(nums) == len(cur) and cur not in res:
                res.append(cur[:])
            for i in range(len(nums)):
                if i not in res1:
                    res1.append(i)
                    cur.append(nums[i])
                    dfs( cur)  
                    cur.pop() 
                    res1.pop()
        for i in range(len(nums)): 
            res1 = [i]
            dfs([nums[i]])
        return res