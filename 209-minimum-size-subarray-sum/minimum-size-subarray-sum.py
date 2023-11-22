class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum = 0
        i = 0
        j = 0
        mini = math.inf
        while j < len(nums):
            currentSum += nums[j]
            if currentSum >= target:
                while currentSum >= target:
                    mini = min(mini, j - i + 1)
                    currentSum -= nums[i]
                    i += 1
            j += 1
        if mini == math.inf:
            return 0
        return mini