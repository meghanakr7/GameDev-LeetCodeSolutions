class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        row_max = []
        col_max = []
        for i in range(len(grid)):
            row_max.append(max(grid[i]))
        for j in range(len(grid[0])):
            # print("Col i s", grid[0:n][j])
            col_max.append(max(row[j] for row in grid))
        # print("row max and col max are ",row_max, col_max)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print("Comparing with ",row_max[j],col_max[j])
                count += min(row_max[i], col_max[j]) - grid[i][j]
        print("Count is ",count)
        return count
                
        