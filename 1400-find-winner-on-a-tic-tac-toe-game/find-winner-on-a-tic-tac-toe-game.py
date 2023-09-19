class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [['' for i in range(3)] for i in range(3)]
        player = 'A'
        i = 0
        while i < len(moves):
            if player == 'A':
                grid[moves[i][0]][moves[i][1]] = 'X'
                player = 'B'
            elif player == 'B':
                grid[moves[i][0]][moves[i][1]] = 'O'
                player = 'A'
            i += 1
        if grid[0][0] == grid[0][1] == grid[0][2]:
            if grid[0][0] == 'X':
                return 'A'
            elif grid[0][0] == 'O':
                return 'B'
        if grid[1][0] == grid[1][1] == grid[1][2]:
            if grid[1][0] == 'X':
                return 'A'
            elif grid[1][0] == 'O':
                return 'B'
        if grid[2][0] == grid[2][1] == grid[2][2]:
            if grid[2][0] == 'X':
                return 'A'
            elif grid[2][0] == 'O':
                return 'B'
        if grid[0][0] == grid[1][0] == grid[2][0]:
            if grid[0][0] == 'X':
                return 'A'
            elif grid[0][0] == 'O':
                return 'B'
        if grid[0][1] == grid[1][1] == grid[2][1]:
            if grid[0][1] == 'X':
                return 'A'
            elif grid[0][1] == 'O':
                return 'B'
        if grid[0][2] == grid[1][2] == grid[2][2]:
                if grid[0][2] == 'X':
                    return 'A'
                elif grid[0][2] == 'O':
                    return 'B'
        if grid[0][0] == grid[1][1] == grid[2][2]:
                if grid[0][0] == 'X':
                    return 'A'
                elif grid[0][0] == 'O':
                    return 'B'
        if grid[0][2] == grid[1][1] == grid[2][0]:
                if grid[0][2] == 'X':
                    return 'A'
                elif grid[0][2] == 'O':
                    return 'B'
        if len(moves)>=9:
            return 'Draw'
        return 'Pending'
        
            