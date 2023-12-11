class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr)*(0.25)
        unique = list(set(arr))
        count = 0
        prev = -1
        for i in range(len(arr)):
            print('prev and unique ',prev, arr[i])
            if arr[i] == prev:
                count += 1
            else:
                count = 1
            print('count is ',count)
            if count > quarter:
                return arr[i]
            prev = arr[i]
    
        

        