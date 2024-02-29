class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l = []
        m = len(grid)
        n = len(grid[0])
        s = set(range(m*n+1))
        total = 0
        length = m*n
        actualSum = 0
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total += grid[i][j]
                if grid[i][j] not in s:
                    repeated = grid[i][j]
                    total -= grid[i][j]
                else:
                    s.remove(grid[i][j])
        print('length is ',length, (length+1), (length+1)//2, length*(length+1)//2)
        actualSum = length*(length+1)//2
        print('total is ',total, actualSum)
        print('diff is ', abs(actualSum - total))
        print('repeated si ',repeated)
        res.append(repeated)
        res.append(abs(actualSum - total))
        print('res is ',res)
        return res



        
        