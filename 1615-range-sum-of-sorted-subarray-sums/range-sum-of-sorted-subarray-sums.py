class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        sumres = []
        cur = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sumres.append(sum(nums[i:j+1]))
        sumres.sort()
        return sum(sumres[left-1: right]) % (10**9 + 7)


        