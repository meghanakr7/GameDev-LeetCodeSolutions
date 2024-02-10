class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        count = 0
        def palindromeCheck(s):
            if s == s[::-1]:
                return True
        def generateSubstrings(s,index):
            for i in range(len(s[index:])):
                res.append(s[index:index+i+1])
                

        for i in range(len(s)):
            generateSubstrings(s, i)
        for i in range(len(res)):
            if palindromeCheck(res[i]):
                count += 1
        # print('res is ',res,count)
        return count
            
        