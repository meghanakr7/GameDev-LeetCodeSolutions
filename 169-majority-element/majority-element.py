class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        nums.sort()
        i = 1
        count = 1
        prev = nums[0]
        maxi = -math.inf
        print("nums are ",nums)
        while i < len(nums):
            if prev == nums[i]:
                count += 1
            else:
                if(count > maxi):
                    maxi = count
                    maxiNum = prev
                count = 1
            prev = nums[i]
            i += 1
        if(count > maxi):
            maxi = count
            maxiNum = prev
        return maxiNum