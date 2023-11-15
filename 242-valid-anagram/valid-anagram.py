class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict()
        if len(s) != len(t):
            return False
        for i in range(len(t)):
            if t.count(t[i]) != s.count(t[i]):
                return False
        return True