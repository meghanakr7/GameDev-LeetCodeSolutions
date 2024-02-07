class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if pivot > nums[i]:
                res.append(nums[i])
        for i in range(len(nums)):
            if pivot == nums[i]:
                res.append(nums[i])
        for i in range(len(nums)):
            if pivot < nums[i]:
                res.append(nums[i])
        # print('res is ',res)
        return res
        