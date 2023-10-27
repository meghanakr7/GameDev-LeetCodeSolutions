class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        maxi = -math.inf
        maxiInd = -1
        while low <= high:
            if arr[low] > maxi:
                maxi = arr[low]
                maxiInd = low
            if arr[high] > maxi:
                maxi = arr[high]
                maxiInd = high
            low += 1
            high -= 1
        return maxiInd
        
        