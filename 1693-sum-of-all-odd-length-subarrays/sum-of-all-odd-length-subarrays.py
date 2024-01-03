class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = 1
        totalSum = 0
        while length <= len(arr):
            for i in range(len(arr)):
                if ((i + length - 1) < len(arr)):
                    totalSum += sum(arr[i:i+length])
            length += 2
        print('totalSum ',totalSum)
        return totalSum


