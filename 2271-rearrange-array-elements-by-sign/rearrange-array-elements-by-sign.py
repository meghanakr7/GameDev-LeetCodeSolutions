class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        for i in range(len(nums)):
            if nums[i] > 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        i = 0
        j = 0
        k = 0
        res = []
        while i < len(nums):
            res.append(positive[j])
            res.append(negative[k])
            i += 2
            j += 1
            k += 1
        print('res is ',res)
        return res
