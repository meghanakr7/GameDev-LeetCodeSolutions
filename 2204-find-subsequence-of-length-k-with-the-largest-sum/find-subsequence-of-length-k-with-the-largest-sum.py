class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        modifiedNums = []
        for i in range(len(nums)):
            modifiedNums.append(nums[i]*-1)
        heapq.heapify(modifiedNums)
        # print('nums is ',modifiedNums)
        totalSum = 0
        allNums = []
        while k:
            allNums.append(-1 * heapq.heappop(modifiedNums))
            k -= 1
        finalList = []
        # return allNums
        for i in range(len(nums)):
            if nums[i] in allNums:
                finalList.append(nums[i])
                allNums.remove(nums[i])
        return finalList

        