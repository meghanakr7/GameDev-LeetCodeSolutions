class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        countOnes = 0
        countZeroes = 0
        maxi = -math.inf
        zeroIndex = 0
        enter = 0
        while j < len(nums):
            if nums[j] == 1:
                countOnes += 1
            else:
                enter = 1
                maxi = max(maxi, countOnes)
                if countZeroes == 1:
                    prevOnes = j - zeroIndex - 1
                    countOnes = prevOnes
                zeroIndex = j
                countZeroes = 1
            j += 1
        maxi = max(maxi, countOnes)
        if not enter:
            return maxi - 1
        return maxi
