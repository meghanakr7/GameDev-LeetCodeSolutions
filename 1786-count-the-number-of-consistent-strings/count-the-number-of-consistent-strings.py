class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set()
        count = 0
        for i in range(len(words)):
            c = 0
            for j in range(len(words[i])):
                if words[i][j] in allowed:
                    c += 1
            if c == len(words[i]):
                count += 1
        return count
        