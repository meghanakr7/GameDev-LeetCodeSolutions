class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            index = word.index(ch)
            newWord = word[0:index+1][::-1] + word[index+1: len(word)]
        # print('newWord is ',newWord)
        return newWord