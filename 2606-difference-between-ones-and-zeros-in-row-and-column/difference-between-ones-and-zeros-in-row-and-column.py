class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0]*n for i in range(m)]
        def countOnes():
            onesRow = []
            zerosRow = []
            for i in range(m):
                print('va is ',grid[i].count(1))
                onesRow.append(grid[i].count(1))
                zerosRow.append(grid[i].count(0))
            countOnes = 0
            countZeros = 0
            onesCol = []
            zerosCol = []
            for i in range(n):
                countOnes = 0
                countZeros = 0
                for j in range(m):
                    if grid[j][i] == 1:
                        countOnes += 1
                    if grid[j][i] == 0:
                        countZeros += 1
                onesCol.append(countOnes)
                zerosCol.append(countZeros)
            print('onesRow is ',onesRow,zerosRow)
            print('cols are ',onesCol, zerosCol)

            res = [[0]*n for i in range(m)]
            for i in range(m):
                for j in range(n):
                    res[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
            print('res is ',res)
            return res
        return countOnes()
        
            
        # for i in range(m):
        #     for j in range(n):
        #         res[i][j] = ans(i,j)

        