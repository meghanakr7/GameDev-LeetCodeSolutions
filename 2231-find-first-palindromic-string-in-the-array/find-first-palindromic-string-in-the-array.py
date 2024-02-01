class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            l = 0
            r = len(words[i]) - 1
            while l < r:
                print('l and r ',l,r)
                if words[i][l] == words[i][r]:
                    l += 1
                    r -= 1
                else:
                    break
            if l >= r:
                return words[i]
        return ""
        