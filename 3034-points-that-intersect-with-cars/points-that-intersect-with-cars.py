class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        arr = [0]*101
        count = 0
        for i in range(len(nums)):
            start = nums[i][0]
            end = nums[i][1]
            for j in range(start, end + 1):
                if not arr[j]:
                    arr[j] = 1
                    count += 1
        # print('arr is ',arr)
        # print('count is ',count)
        return count
