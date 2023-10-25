class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        indexes = []
        res = []
        cur = []
        nums.sort()
        def dfs(ind, cur):
            print("CUr is ",ind,cur,indexes)
            
            if cur not in res:
                res.append(cur[:])
            if len(cur) == len(nums):
                return
            for i in range(ind, len(nums)):
                if i not in indexes:
                    print("I is not in indexes ",i,indexes,cur)
                    indexes.append(i)
                    cur.append(nums[i])
                    dfs(i +1, cur)
                    cur.pop()
                    indexes.pop()
        for i in range(len(nums)):
            indexes.append(i)
            cur.append(nums[i])
            print("Index and cur are ",indexes, cur)
            dfs(i, cur)
            indexes = []
            cur = []
        # if nums not in res:
        #     res.append(nums)
        res.append([])
        print("Res is ",res)  
        return res
