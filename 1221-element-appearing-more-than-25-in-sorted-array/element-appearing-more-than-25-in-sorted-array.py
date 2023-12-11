class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr)*(0.25)
        count = 0
        prev = -1
        for i in range(len(arr)):
            if arr[i] == prev:
                count += 1
            else:
                count = 1
            if count > quarter:
                return arr[i]
            prev = arr[i]
    
        

        