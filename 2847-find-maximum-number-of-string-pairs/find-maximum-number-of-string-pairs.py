class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        for ind, word in enumerate(words):
            revword = word[::-1]
            if len(word) and revword in words and words.index(revword) != words.index(word):
                count += 1
                words[ind] = ""
                words[words.index(revword)] = ""
        return count
                