class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        words = list(s)
        print('words are ',words)
        for i in range(len(indices)):
            tempWord = s[indices[i]: len(sources[i]) + indices[i]]
            tempLen = len(sources[i])
            print('tempWord ',tempWord)
            if(tempWord == sources[i]):
                words[indices[i]] = targets[i]
                while tempLen != 1:
                    tempindex = indices[i]+tempLen-1
                    words[tempindex] = ''
                    tempLen -= 1
                
        print('words are ',words, "".join(words))
        return "".join(words)

