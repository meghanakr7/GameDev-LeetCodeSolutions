class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        revString = ""
        revWords = words[::-1]
        while ('' in revWords):
            revWords.remove('')
        revString += revWords[0]
        for i in range(1, len(revWords)):
            if len(revWords[i]):
                revString += " "
                revString += revWords[i]
        return revString