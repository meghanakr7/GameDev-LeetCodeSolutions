class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        newString = ""
        i = 0
        
        while len(s) > len(newString) and i < len(words):
            # print('nw Str ',newString)
            newString += words[i]
            if(newString == s[0:len(newString)]):
                if(newString == s):
                    return True
                i += 1
                continue
            else:
                return False
            i += 1
        # print('new String ', newString)
        return False

        