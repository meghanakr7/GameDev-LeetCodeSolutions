class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        startChar = s[0]
        l = []
        count = 1
        for i in range(1, len(s)):
            if(s[i] == startChar):
                count += 1
            if(s[i] != startChar):
                l.append(count)
                count = 1
                startChar = s[i]
        l.append(count)
        print('l is ',l)
        res = 0
        for i in range(len(l)-1):
            res += min(l[i], l[i+1])
        print('res is ',res)
        return res
        # for i in range(len(l)):
