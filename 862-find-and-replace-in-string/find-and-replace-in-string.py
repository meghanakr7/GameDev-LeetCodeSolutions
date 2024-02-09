class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        words = list(s)
        for i in range(len(indices)):
            tempWord = s[indices[i]: len(sources[i]) + indices[i]]
            tempLen = len(sources[i])
            if(tempWord == sources[i]):
                words[indices[i]] = targets[i]
                while tempLen != 1:
                    tempindex = indices[i]+tempLen-1
                    words[tempindex] = ''
                    tempLen -= 1
        return "".join(words)

