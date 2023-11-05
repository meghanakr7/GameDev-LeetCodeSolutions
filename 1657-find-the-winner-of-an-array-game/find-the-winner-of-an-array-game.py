class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win_count = 0
        prev = -1
        winner = -1
        i = 0
        j = i + 1
        n = len(arr)
        if len(arr) < k:
            return max(arr)
        while win_count < k:
            if arr[i] < arr[j]:
                winner = arr[j]
                j = (j + 1)%n
                i = (j - 1)%n
            else:
                winner = arr[i]
                j = (j + 1)%n
            if winner == prev:
                win_count += 1
            else:
                win_count = 1
            print("winner :i, j", winner, i, j, win_count)
            prev = winner
        return winner
            
            