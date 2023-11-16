class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 0
        j = 0
        goodString = []
        count = 0
        while j < len(s):
            goodString.append(s[j])
            if j - i + 1 == 3:
                if len(set(goodString)) == 3:
                    count += 1
                goodString = goodString[1:len(goodString)]
                i += 1
            j += 1
        return count

        