class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        if len(nums) < 2:
            return -1
        # if len(nums) == 3:
        #     if(nums[0] + nums[1] < nums[2]):
        #         return -1
        #     else:
        #         return sum(nums)
        print(nums)
        i = 0
        total = 0
        while i < len(nums):
            print(nums[i], sum(nums[i+1:]))
            if(nums[i] < sum(nums[i+1:])):
                total = nums[i] + sum(nums[i+1:])
                break
            i += 1
        print('total is ',total)
        if(total == 0):
            return -1
        return total






        

        