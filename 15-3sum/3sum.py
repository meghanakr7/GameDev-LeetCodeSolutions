class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        s = set()
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tripletSum = nums[i] + nums[j] + nums[k]
                if tripletSum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif tripletSum > target:
                    k -= 1
                else:
                    j += 1
        return list(s)