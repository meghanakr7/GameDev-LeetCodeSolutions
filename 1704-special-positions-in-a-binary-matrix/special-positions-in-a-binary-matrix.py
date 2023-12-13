class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        def checkRow(row, col):
            for i in range(m):
                if i!=row and mat[i][col] == 1:
                    return False
            return True
        def checkCol(row, col):
            for j in range(n):
                if j!=col and mat[row][j] == 1:
                    return False
            return True
    
        finalRes = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if (checkRow(i, j) and checkCol(i, j)):
                        finalRes += 1
        return finalRes


                    