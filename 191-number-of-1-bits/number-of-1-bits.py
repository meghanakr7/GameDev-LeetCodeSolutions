class Solution:
    def hammingWeight(self, n: int) -> int:
        print('n',n)
        count = 0
        strn = str(bin(n))[2:]
        print('str ',strn)
        for i in range(len(strn)):
            if strn[i] == '1':
                count += 1
        print('count is ',count)
        return count