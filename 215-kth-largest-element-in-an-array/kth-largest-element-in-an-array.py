class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-ele for ele in nums]
        print("arr is ",arr)
        heapq.heapify(arr)
        for i in range(k-1):
            heapq.heappop(arr)
        # print("val is ", heapq.heappop(arr))
        return -1 * heapq.heappop(arr)