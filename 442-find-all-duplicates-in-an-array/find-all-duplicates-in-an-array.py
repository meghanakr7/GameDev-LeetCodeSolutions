class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = 0
        result = []
        for i in range(len(nums)):

            if(nums[abs(nums[i]) -1]< 0):
                result.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1] = -1 * nums[abs(nums[i])-1]
        return result
        