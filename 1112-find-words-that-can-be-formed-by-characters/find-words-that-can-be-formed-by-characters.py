class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        no = False
        count = 0
        for i in range(len(words)):
            charsTemp = []
            charsTemp[:0] = chars
            no = False
            for j in range(len(words[i])):
                l = len(words[i])
                if words[i][j] in charsTemp:
                    charsTemp.remove(words[i][j])
                else:
                    no = True
                    break
            if(not no):
                count += l
        return count

            

        