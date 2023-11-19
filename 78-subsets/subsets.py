class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(ind, cur):
            if len(cur) > len(nums):
                return
            res.append(cur)
            for i in range(ind, len(nums)):
                if nums[i] not in cur:
                    dfs(i, cur + [nums[i]])
        dfs(0, [])
        print("res is ",res)
        return res