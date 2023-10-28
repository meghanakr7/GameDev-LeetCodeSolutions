class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # actualLen = (len(nums) * (len(nums) + 1)) // 2
        # actual = ((len(nums)-1) * len(nums)) //2

        # givenLen = sum(nums)
        # print("actual len",actualLen, givenLen,actual)
        # return abs(actual - givenLen)
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
