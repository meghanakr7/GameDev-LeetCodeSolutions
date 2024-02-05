class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = -1
        m = [0] * 26
        ones = []
        i = 0
        act = s
        while i < len(s):
            if(s[i]!='_'):
                m[ord(s[i])-ord('a')] += 1
                if m[ord(s[i])-ord('a')] == 1:
                    ones.append(s[i])
                if m[ord(s[i])-ord('a')] > 1:
                    ones.remove(s[i])
                    s = s.replace(s[i],"_")
                    print('s[i] and s',s[i],s)
            i += 1
        print('ones are ',ones)
        if(len(ones) == 0):
            return -1
        return act.index(ones[0])

            
        