class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0 
        nums.sort()
        total = 0
        fin = 1
        while j < len(nums):
            total += nums[j]
            maxi = nums[j]
            while total + k < maxi * (j - i + 1):
                total -= nums[i]
                i += 1
            fin = max(fin, j - i + 1)
            j += 1
        return fin
