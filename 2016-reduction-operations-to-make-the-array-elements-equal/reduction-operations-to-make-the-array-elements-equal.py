class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        d = {}
        numsSet = list(set(nums))
        numsSet.sort()
        s = 0
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        keys = list(d.keys())
        for i in range(1, len(keys)):
            s += i * d[keys[i]]
        return s

        