class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        pascal = [[0]*i for i in range(1, numRows+1)]
        pascal[0] = [1]
        pascal[1] = [1,1]
        for i in range(2,numRows):
            row = i
            pascal[i] = [0]*(row+1)
            pascal[i][0] = 1
            pascal[i][row] = 1
            for j in range(1, row):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal
                

