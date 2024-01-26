class Solution:
    def maxScore(self, s: str) -> int:
        nz = 0
        no = 0
        if s[0] == '0':
            nz += 1
        no = s[1:].count('1')
        maxi = nz + no
        for i in range(1, len(s)-1):
            print('for i, s[i]',i, s[i])
            if s[i] == '0':
                nz += 1
            else:
                no -= 1
            print('for this i, maxi is ',i, nz, no, nz + no)
            if maxi < (nz + no):
                maxi = nz + no
        print('maxi is ',maxi)
        return maxi
            
            

        
        