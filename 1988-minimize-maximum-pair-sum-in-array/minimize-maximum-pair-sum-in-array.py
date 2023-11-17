class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxiSum = 0
        n = len(nums)
        for i in range(len(nums)//2):
            maxiSum = max(nums[i] + nums[n-i-1], maxiSum)
        print("maxiSum is ",maxiSum)
        return maxiSum

