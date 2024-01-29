class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        hourGlass = []
        maxi = -1
        for i in range(m-2):
            for j in range(n-2):
                maxi = max(maxi, sum([grid[i][j], grid[i][j+1], grid[i][j+2], grid[i+1][j+1], grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]))
        return maxi


        