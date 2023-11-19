class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        d = {}
        numsSet = list(set(nums)) # Duplicates
        numsSet.sort()
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        s = 0
        keys = list(d.keys())
        # print("nums srot ",sorted(nums))
        # print("keys are ",keys)
        print("d is ",d)
        for i in range(1, len(keys)):
            s += i * d[keys[i]]
        return s

        