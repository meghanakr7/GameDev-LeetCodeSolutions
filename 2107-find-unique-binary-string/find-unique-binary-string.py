class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        i = 0
        s = ""
        for i in range(0, pow(2,n)):
            s1 = bin(i)[2:]
            while len(s1) < n:
                s1 = "0" + s1
            if s1 in nums:
                continue
            else:
                return s1