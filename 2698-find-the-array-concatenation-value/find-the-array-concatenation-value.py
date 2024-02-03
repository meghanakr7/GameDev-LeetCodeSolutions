class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        concat = ""
        currentSum = 0
        while l < r:
            concat += str(nums[l]) + str(nums[r])
            currentSum += int(concat)
            l += 1
            r -= 1
            concat = ''
        # print('current sum is ',currentSum)
        if l == r:
            currentSum += nums[l]
        # print('final sum is ', currentSum)
        return currentSum

        