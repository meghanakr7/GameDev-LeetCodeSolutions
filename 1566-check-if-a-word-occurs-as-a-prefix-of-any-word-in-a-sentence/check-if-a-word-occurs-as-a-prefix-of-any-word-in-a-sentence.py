class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        allWords = sentence.split(' ')
        print('allWords are ',allWords)
        res = -1
        for i in range(len(allWords)):
            # print('words is ',allWords[i], allWords[i][0:len(searchWord)])
            if allWords[i][0:len(searchWord)] == searchWord:
                res = i
                break
        if res == -1:
            return -1
        else:
            return res + 1