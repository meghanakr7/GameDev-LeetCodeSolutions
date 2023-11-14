class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        fIndex = 0
        sIndex = 0
        newStr = ""
        while fIndex < len(word1) and sIndex < len(word2):
            newStr += word1[fIndex]
            fIndex += 1
            newStr += word2[sIndex]
            sIndex += 1
        if fIndex < len(word1):
            newStr += word1[fIndex : len(word1)]
        if sIndex < len(word2):
            newStr += word2[sIndex : len(word2)] 
        print("newStr is ",newStr)
        return newStr
        