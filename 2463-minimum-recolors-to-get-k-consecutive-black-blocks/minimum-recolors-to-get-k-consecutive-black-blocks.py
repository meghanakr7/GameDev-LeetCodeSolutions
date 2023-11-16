class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        j = 0
        black = 0
        maxiBlack = 0
        while j < len(blocks):
            if blocks[j] == 'B':
                black += 1
            if j - i + 1 == k:
                maxiBlack = max(maxiBlack, black)
                if blocks[i] == 'B':
                    black -=1
                i += 1
            j += 1
        # print("maxi Blacks are ",maxiBlack)
        # print("k is ",k)
        return k - maxiBlack


        