class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
            for i in range(len(nums)):
                if nums[i] not in cur:
                    cur.append(nums[i])
                    dfs(cur)
                    cur.pop()
        for i in range(len(nums)):

            cur.append(nums[i])
            # print("Befor starting dfs cur is ",cur)
            dfs(cur)
            # print("AFter first iteration res is ",res)
            cur = []
        # print("Res is ",res)
        return res
        