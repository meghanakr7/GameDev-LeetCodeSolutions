class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        s = [0]*2
        s[0] = grid[0][0]
        priorityQ = [(grid[0][0], 0, 0)]
        currentSum = 0
        # while priorityQ:
        #     val, i, j = heapq.heappop(priorityQ)
        #     if i == m-1 and j == n - 1:
        #         currentSum = val
        #         break
        #     if i+1>=0 and i+1<m and j>=0 and j<n:
        #         heapq.heappush(priorityQ, (val + grid[i+1][j], i+1, j))
        #     if i>=0 and i<m and j+1>=0 and j+1<n:
        #         heapq.heappush(priorityQ, (val + grid[i][j+1], i, j+1))
        #     visited.add((i, j))
        # return currentSum
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for i in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        print("grid is ",dp)
        return dp[m-1][n-1]

        for i in range(m):
            for j in range(n):
                dp[i]