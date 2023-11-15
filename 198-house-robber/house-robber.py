class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memoize = [0]*n
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        memoize[0] = nums[0]
        memoize[1] = nums[1]
        memoize[2] = nums[0] + nums[2]
        for i in range(3, len(nums)):
            memoize[i] = max(memoize[0:i-1]) + nums[i]
        return max(memoize)