class Solution:
    def maxScore(self, s: str) -> int:
        nz = 0
        no = 0
        if s[0] == '0':
            nz += 1
        no = s[1:].count('1')
        maxi = nz + no
        for i in range(1, len(s)-1):
            if s[i] == '0':
                nz += 1
            else:
                no -= 1
            if maxi < (nz + no):
                maxi = nz + no
        return maxi
            
            

        
        