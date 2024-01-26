class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        sortedWords = ['']*len(words)
        print(sortedWords)
        for i in range(len(words)):
            index = words[i][-1]
            # print('index is ',index)
            sortedWords[int(index)-1] = words[i][:-1]
        print('sortedWords are ',sortedWords, ' '.join(sortedWords))
        # return sortedWords.join(' ')
        return ' '.join(sortedWords)


        