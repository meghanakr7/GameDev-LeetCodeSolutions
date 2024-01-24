class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        spaces = 0
        words = s.split(' ')
        output = ''
        i = 0
        while spaces < k and i < len(words):
            output += words[i]
            if spaces != k - 1:
                output += ' '
            spaces += 1
            i += 1
        return output


        