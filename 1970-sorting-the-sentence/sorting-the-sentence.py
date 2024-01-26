class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        sortedWords = ['']*len(words)
        for i in range(len(words)):
            index = words[i][-1]
            sortedWords[int(index)-1] = words[i][:-1]
        return ' '.join(sortedWords)


        