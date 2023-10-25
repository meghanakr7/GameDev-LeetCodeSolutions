class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        indexes = []
        def dfs(cur):
            if len(nums) == len(cur) and cur not in res:
                res.append(cur[:])
            for i in range(len(nums)):
                if i not in indexes:
                    indexes.append(i)
                    cur.append(nums[i])
                    dfs( cur)  
                    cur.pop() 
                    indexes.pop()
        for i in range(len(nums)): 
            indexes = [i]
            dfs([nums[i]])
        return res