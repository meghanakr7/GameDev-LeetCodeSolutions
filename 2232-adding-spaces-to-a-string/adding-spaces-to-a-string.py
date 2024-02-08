class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        k = 0
        finalStr = ''
        for i in range(len(s)):
            if k < len(spaces) and i == spaces[k]:
                finalStr += ' '
                k += 1
            finalStr += s[i]
        # print('final str is ',finalStr)
        return finalStr
