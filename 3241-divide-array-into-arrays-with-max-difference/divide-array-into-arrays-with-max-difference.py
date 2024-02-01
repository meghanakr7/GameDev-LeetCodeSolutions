class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums)%3!=0:
            return []
        nums.sort()
        res = []
        for i in range(0, len(nums)-2, 3):
            if (abs(nums[i] - nums[i+1]) <= k and abs(nums[i] - nums[i+2]) <= k and abs(nums[i+1] - nums[i+2]) <= k):
                res.append([nums[i], nums[i+1], nums[i+2]])
            else:
                return []
        return res
        