class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        no = False
        count = 0
        for i in range(len(words)):
            charsTemp = []
            charsTemp[:0] = chars
            no = False
            print('word is ',words[i],charsTemp)
            for j in range(len(words[i])):
                l = len(words[i])
                print('word is ',words[i][j])
                if words[i][j] in charsTemp:
                    print('word is ',words[i])
                    charsTemp.remove(words[i][j])
                else:
                    print('word is ',words[i])
                    no = True
                    break
            if(not no):
                count += l
        return count

            

        