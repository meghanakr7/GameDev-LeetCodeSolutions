class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr)*(0.25)
        unique = list(set(arr))
        for i in range(len(unique)):
            if arr.count(unique[i]) > quarter:
                return unique[i]
        