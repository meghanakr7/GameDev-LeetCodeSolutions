class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        count = 0
        def createSubStrings(index):
            for i in range(len(s[index:])):
                res.append(s[index:index+i+1])

        for i in range(len(s)):
            createSubStrings(i)
        # print('res is ',res)
        for i in range(len(res)):
            if(res[i] == res[i][::-1]):
                count += 1
        
        print('Count is ',count)
        return count