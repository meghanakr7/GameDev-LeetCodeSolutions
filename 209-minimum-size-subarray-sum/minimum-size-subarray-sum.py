class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        currentSum = 0
        mini = math.inf
        seen = []
        while j < len(nums):
            currentSum += nums[j]
            seen.append(nums[j])
            if currentSum >= target:
                while currentSum >= target:
                    mini = min(j - i + 1, mini)
                    currentSum -= nums[i]
                    i += 1
            j += 1
        print("mini is ",mini-1)
        if mini == math.inf:
            return 0
        return mini