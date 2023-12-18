class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        print('nums is ',nums)
        return  nums[-1]*nums[-2] - nums[0]*nums[1]