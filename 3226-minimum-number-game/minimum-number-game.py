class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        nums.sort()
        output = []
        while i < n:
            first = nums[0]
            if nums[1]:
                sec = nums[1]
                output.append(sec)
            output.append(first)
            nums = nums[2:]
            i += 2
        return output

        