class Solution:
    def repeatedCharacter(self, s: str) -> str:
        alpha = [0]*26
        for i in s:
            if alpha[ord(i) - ord('a')]:
                return i
            else:
                alpha[ord(i) - ord('a')] = 1
