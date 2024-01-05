class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        prefixSum = [0] * n
        prefixSum[0] = nums[0]
        res = []
        for j in range(1, n):
            prefixSum[j] = nums[j] + prefixSum[j-1]
        
        for i in range(len(queries)):
            enter = 0
            for j in range(n):
                if prefixSum[j] > queries[i]:
                    enter = 1
                    res.append(j)
                    break
            if(enter == 0):
                res.append(n)
        return res
