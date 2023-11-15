class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = 0
        permutation = ""
        def check(s):

            for i in range(len(s)):
                if s.count(s[i]) != s1.count(s[i]):
                    return False
            return True

        while j < len(s2): 
            permutation += s2[j]
            if len(permutation) == len(s1):
                if check(permutation):
                    return True
                permutation = permutation[1:len(permutation)]
                i += 1
            j+=1
        return False

        