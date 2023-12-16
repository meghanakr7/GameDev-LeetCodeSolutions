class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        e = {}
        for i in range(26):
            d[chr(ord('a')+i)] = 0
            e[chr(ord('a')+i)] = 0
        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1
        for char in t:
            if char not in e:
                e[char] = 0
            e[char] += 1
        for i in range(26):
            print('val is ',ord('a'))
            print('val is ',chr(ord('a')+i))
            # if chr(ord('a')+i) in d and chr(ord('a')+i) in e:
            if d[chr(ord('a')+i)] != e[chr(ord('a')+i)]:
                return False
        return True
            

        