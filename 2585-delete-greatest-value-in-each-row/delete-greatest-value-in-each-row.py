class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        val = math.inf
        for i in range(m):
            for j in range(n):
                grid[i][j] = -1 * grid[i][j]
        for i in range(len(grid)):
            heapq.heapify(grid[i])
        # print("new grid is ",grid)
        res = 0
        for j in range(n):
            val = math.inf
            for i in range(len(grid)):
                val = min(val, heapq.heappop(grid[i]))
            #     print("even after popping ",grid)
            # print("val is ",val)
            res += (-1 * val)
        # print("res is ",res)
        return res
        
