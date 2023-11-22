class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = -1  * nums[i]
        heapq.heapify(nums)
        i = 0
        n = len(nums)
        return (-1 * heapq.heappop(nums) - 1) * (-1 * heapq.heappop(nums) - 1)