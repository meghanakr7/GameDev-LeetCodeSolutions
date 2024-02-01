class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        chars = list(s)
        count = 0
        while l < r:
            if(s[l] < s[r]):
                chars[r] = s[l]
                count += 1
            elif(s[l] > s[r]):
                chars[l] = s[r]
                count += 1
            l += 1
            r -= 1
        return ''.join(chars)


        