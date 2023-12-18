class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        prefix_sum = 0
        result = 0
        
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in d:
                result += d[prefix_sum - k]
            if prefix_sum in d:
                d[prefix_sum] += 1
            else:
                d[prefix_sum] = 1
        return result