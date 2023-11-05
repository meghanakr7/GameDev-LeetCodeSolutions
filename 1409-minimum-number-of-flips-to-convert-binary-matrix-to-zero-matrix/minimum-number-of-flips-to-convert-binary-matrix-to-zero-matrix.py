class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        isFinalState = True
        q = deque([])
        q.append((tuple(tuple(row for row in mat)), 0))
        def flip(r, c, temp):
            ans = deepcopy(temp)
            ans[r][c] ^= 1
            if r + 1 < len(ans):
                ans[r+1][c] ^=1
            if r - 1 >= 0:
                ans[r-1][c] ^= 1
            if c + 1 < len(ans[0]):
                ans[r][c+1] ^= 1
            if c - 1 >= 0:
                ans[r][c-1] ^= 1
            return ans
        visited = set()
        while q:
            isFinalState = True
            tempState, numSteps = q.popleft()
            for row in range(len(tempState)):
                for col in range(len(tempState[0])):
                    if tempState[row][col] == 1:
                        isFinalState = False
                        break
            if isFinalState:
                return numSteps
            for row in range(len(mat)):
                for col in range(len(mat[0])):
                    t = flip(row, col, tempState)
                    if (tuple(tuple(row) for row in t)) not in visited:
                        q.append((t, numSteps + 1))
                        visited.add(tuple(tuple(row) for row in t))
        return -1

        