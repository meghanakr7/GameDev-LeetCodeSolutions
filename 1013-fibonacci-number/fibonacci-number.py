class Solution:
    def fib(self, n: int) -> int:
        allArr = [0]*(n+1)
        if n == 0 or n == 1:
            return n
        allArr[0] = 0
        allArr[1] = 1
        for i in range(2, n+1):
            allArr[i] = allArr[i-1] + allArr[i-2]
        return allArr[n]
        
        