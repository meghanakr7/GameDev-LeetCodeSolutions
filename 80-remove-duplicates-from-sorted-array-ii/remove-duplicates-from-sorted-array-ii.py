class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        indexes = []
        count = 0
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = 1
            elif d[num] == 2:
                nums[i] = '_'
                count += 1
                indexes.append(i)
            else:
                d[num] += 1
        while '_' in nums:
            nums.remove('_')
        return len(nums)

        