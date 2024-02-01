class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        print('len i s ',len(nums))
        if len(nums)%3!=0:
            return []
        nums.sort()
        res = []
        print('nums are ',nums)
        for i in range(0, len(nums)-2, 3):
            print('nums [i]', nums[i], nums[i+1],abs(nums[i] - nums[i+1]), abs(nums[i] - nums[i+2]), abs(nums[i+1] - nums[i+2]) )
            if (abs(nums[i] - nums[i+1]) <= k and abs(nums[i] - nums[i+2]) <= k and abs(nums[i+1] - nums[i+2]) <= k):
                res.append([nums[i], nums[i+1], nums[i+2]])
            else:
                print(nums[i])
                return []
        print('res is ',res)
        return res
        