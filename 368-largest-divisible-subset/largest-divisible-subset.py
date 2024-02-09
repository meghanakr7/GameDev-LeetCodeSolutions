class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1]*n
        max_size = 1
        max_index = 0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i
        print('max_size and max_index ',max_size, max_index)
        
        result = []
        num = nums[max_index]
        print('num is ',num,dp)
        for i in range(max_index, -1, -1):
            if num % nums[i] == 0 and dp[i] == max_size:
                num = nums[i]
                max_size -= 1
                result.append(nums[i])
        print('res is ',result)
        return result

