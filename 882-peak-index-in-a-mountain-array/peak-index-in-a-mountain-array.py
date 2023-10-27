class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        mid = 0
        n = len(arr)
        while low <= high:
            mid = (low + high)//2
            if ((mid == 0 or arr[mid-1]) < arr[mid] and (mid == n-1 or arr[mid+1]) < arr[mid]):
                return mid
            elif mid > 0 and arr[mid-1] > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        
        