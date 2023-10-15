class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        index = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] < target:
                index += 1
            if nums[i] == target:
                count += 1
        res = []
        for i in range(index, index+count):
            res.append(i)
        return res