class Solution:
    def knightDialer(self, n: int) -> int:
        prev = [1 for j in range(10)]
        for i in range(1,n):
            curr = [0 for j in range(10)]
            for j in range(10):
                
                curr[0] = prev[4] + prev[6]
                curr[1] = prev[8] + prev[6]
                curr[2] = prev[7] + prev[9]
                curr[3] = prev[4] + prev[8]
                curr[4] = prev[0] + prev[3] + prev[9]
                curr[5] = 0
                curr[6] = prev[7] + prev[1] + prev[0]
                curr[7] = prev[2] + prev[6]
                curr[8] = prev[1] + prev[3]
                curr[9] = prev[4] + prev[2]
            prev = curr
        
        return sum(prev)%1000000007