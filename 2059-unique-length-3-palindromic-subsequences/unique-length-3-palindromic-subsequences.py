class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for alpha in string.ascii_lowercase:
            first, last = s.find(alpha), s.rfind(alpha)
            if first > -1:
                res += len(set(s[first + 1: last]))
        return res