class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i == j or i +j == n-1):
                    if grid[i][j] == 0:
                        print('h1')
                        return False
                    else:
                        continue
                elif grid[i][j] != 0:
                    print('h3',i,j)
                    return False
        return True

        