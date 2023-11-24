class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        first = 0
        last = len(piles) - 1
        sec = first + 1
        mine = 0
        while sec < last:
            mine += piles[sec]
            first = sec + 1
            sec = first + 1
            last -=1
        # print("mine is ",mine)
        return mine