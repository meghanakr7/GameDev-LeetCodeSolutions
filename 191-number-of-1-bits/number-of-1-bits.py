class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        strn = str(bin(n))[2:]
        for i in range(len(strn)):
            if strn[i] == '1':
                count += 1
        return count