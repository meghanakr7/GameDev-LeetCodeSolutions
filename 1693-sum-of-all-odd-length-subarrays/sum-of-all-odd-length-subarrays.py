class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = sum(arr)
        window = 3
        max_window = len(arr) if len(arr)%2 == 1 else len(arr)-1
        cur = 0
        print('initial ans ',ans)
        while window <= max_window:
            localSum = sum(arr[:window])
            ans += localSum
            print('ans is ',ans)
            left = arr[0]
            for i in range(1, len(arr) - window + 1):
                curr = arr[i + window - 1]
                localSum += curr - left
                left = arr[i]
                ans += localSum
            window += 2
        print('ans ',ans)
        return ans
            
