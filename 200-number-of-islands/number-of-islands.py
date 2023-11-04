class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        s = set()
        def bfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or (i,j) in s or grid[i][j] == "0":
                return 0
            s.add((i,j))
            grid[i][j] = "0"
            return bfs(i-1, j) or bfs(i, j-1) or bfs(i, j+1) or bfs(i+1, j)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        return count