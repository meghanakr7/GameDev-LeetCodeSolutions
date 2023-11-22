class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # print("now nus is ",nums)
        
        for i in range(len(nums)):
            nums[i] = -1  * nums[i]
        heapq.heapify(nums)
        i = 0
        n = len(nums)
        # while i < n:
        #     print("val popped is ",heapq.heappop(nums))
        #     i += 1
        return (-1 * heapq.heappop(nums) - 1) * (-1 * heapq.heappop(nums) - 1)