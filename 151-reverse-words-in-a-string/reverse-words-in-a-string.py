class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        # print("words" ,words)
        # print("reverse ",words[::-1])
        revString = ""
        revWords = words[::-1]
        # print("revWordsa are ",revWords)
        for i in range(len(revWords)):
            if '' in revWords:
                # print("After removing ",revWords.remove(''))
                # print("revWords ",revWords)
                revWords.remove('')
        
        revString += revWords[0]
        # print("After first ",revString)
        for i in range(1, len(revWords)):
            if len(revWords[i]):
                revString += " "
                revString += revWords[i]
        # print("revString ",revString)
        return revString