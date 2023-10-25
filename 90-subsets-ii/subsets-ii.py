class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        indexes = []
        res = []
        cur = []
        nums.sort()
        def dfs(ind, cur):
            if cur not in res:
                res.append(cur[:])
            if len(cur) == len(nums):
                return
            for i in range(ind, len(nums)):
                if i not in indexes:
                    indexes.append(i)
                    cur.append(nums[i])
                    dfs(i +1, cur)
                    cur.pop()
                    indexes.pop()
        for i in range(len(nums)):
            indexes.append(i)
            cur.append(nums[i])
            dfs(i, cur)
            indexes = []
            cur = []
        res.append([]) 
        return res
