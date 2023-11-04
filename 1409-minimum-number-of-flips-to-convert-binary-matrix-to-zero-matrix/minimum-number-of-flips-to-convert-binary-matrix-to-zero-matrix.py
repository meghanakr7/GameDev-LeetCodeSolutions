class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        queue.append((mat, 0))
        visited.add(tuple(tuple(row) for row in mat))
        def flip(row, col, state):
            ans = deepcopy(state)
            ans[row][col] ^= 1
            if row - 1 >= 0:
                ans[row-1][col] ^= 1
            if row + 1 < len(state):
                ans[row+1][col] ^= 1
            if col - 1 >= 0:
                ans[row][col-1] ^= 1
            if col + 1 < len(state[0]):
                ans[row][col+1] ^= 1
            return ans
        
        while queue:
            isFinal = True
            curState, numSteps = queue.popleft()
            print("CurState is ",curState)
            for row in range(len(curState)):
                for col in range(len(curState[0])):
                    if curState[row][col] == 1:
                        isFinal = False
                        break
            if isFinal:
                return numSteps
            for row in range(len(curState)):
                for col in range(len(curState[0])):
                    tempState = flip(row, col, curState)
                    if tuple(tuple(row) for row in tempState) not in visited:
                        queue.append((tempState, numSteps + 1))
                        visited.add(tuple(tuple(row) for row in tempState))
        return -1