class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtracking(path):
            if len(path) == len(nums):
                # print("path is ",path,ans)
                ans.append(path[:])
                # print("Now ans is ",ans)
                return 
            for n in nums:
                if n not in path:
                    path.append(n)
                    backtracking(path)
                    path.pop()
        backtracking([])
        return ans
            