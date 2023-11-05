class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        count = 0
        def bfs(i, j, grid):
            if i < 0 or i > m-1 or j < 0 or j >n-1 or ((i, j) in visited) or grid[i][j] != "1":
                return 0
            visited.add((i, j))
            grid[i][j] = "0"
            return bfs(i-1, j, grid) or bfs(i, j-1, grid) or bfs(i+1, j, grid) or bfs(i, j+1, grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j, grid)
        # print("grid is ",grid)
        return count


        