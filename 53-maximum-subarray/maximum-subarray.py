class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dynamicTable = [0] * len(nums)
        dynamicTable[0] = nums[0]
        for i in range(1, len(nums)):
            dynamicTable[i] = max(nums[i], dynamicTable[i-1] + nums[i])
        # print("dynamic Table is ",dynamicTable)
        # print("max is ",max(dynamicTable))
        return max(dynamicTable)