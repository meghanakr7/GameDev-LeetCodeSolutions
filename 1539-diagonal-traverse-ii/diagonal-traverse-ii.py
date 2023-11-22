class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        m = len(nums)
        for i in range(m):
            for j in range(len(nums[i])):
                d[i+j].append(nums[i][j])
        return [v for k in d.keys() for v in reversed(d[k])]