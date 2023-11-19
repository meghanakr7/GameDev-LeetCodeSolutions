class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
            for i in range(len(nums)):
                if nums[i] not in cur:
                    cur.append(nums[i])
                    dfs(cur)
                    cur.pop()
        for i in range(len(nums)):
            dfs([nums[i]])
        return res
