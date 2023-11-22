class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        total = 0
        mini = math.inf
        while j < len(nums):
            total += nums[j]
            if total >= target:
                while total >= target:
                    mini = min(mini, j - i + 1)
                    total -= nums[i]
                    i += 1
            j += 1
        print("mini is ",mini)
        if mini == math.inf:
            return 0
        return mini


        