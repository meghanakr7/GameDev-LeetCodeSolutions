class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zeroes = s.count('0')
        print('ones and zeroes are ',ones,zeroes)
        finalStr = ""
        Ones = ones - 1
        i = 0
        while i < Ones: 
            finalStr += '1'
            i += 1
        i = 0
        while i < zeroes:
            finalStr += '0'
            i += 1
        finalStr += '1'
        print('final res is ',finalStr)
        return finalStr
            