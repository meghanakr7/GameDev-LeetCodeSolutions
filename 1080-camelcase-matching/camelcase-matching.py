class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        trueUpperCases = []
        trueUpperIndices = []
        patternUpperCases = []
        patternUpperIndices = []
        ans = []
        actWords = []
        word = ''
        for i in range(len(pattern)):
            if pattern[i] >= 'A' and pattern[i] <= 'Z':
                actWords.append(word)
                word = ''
                trueUpperCases.append(pattern[i])
                trueUpperIndices.append(i)
            else:
                word += pattern[i]
        actWords.append(word)
        print(actWords)
        # print(trueUpperCases)
        # print(trueUpperIndices)
        for i in range(len(queries)):
            patternUpperCases = []
            patternUpperIndices = []
            patternWords = []
            patternSmall = ''
            for j in range(len(queries[i])):
                if queries[i][j] >= 'A' and queries[i][j] <= 'Z':
                    patternWords.append(patternSmall)
                    patternUpperCases.append(queries[i][j])
                    patternUpperIndices.append(j)
                    patternSmall = ''
                else:
                    patternSmall += queries[i][j]
            patternWords.append(patternSmall)
            if(len(patternUpperCases)!=len(trueUpperCases) or patternUpperCases != trueUpperCases):
                ans.append(False)
            else:
                if(len(actWords) == 0):
                    ans.append(True)
                else:
                    word = queries[i]
                    k = 0
                    while k < len(actWords):
                        if actWords[k]:
                            word1 = actWords[k]
                            word2 = patternWords[k]
                            ind = 0
                            l = 0
                            while l < len(patternWords[k]):
                                if ind < len(word1) and word1[ind] == patternWords[k][l]:
                                    ind += 1
                                l += 1
                            if ind != len(word1):
                                break
                        k += 1
                    if k == len(actWords):
                        ans.append(True)
                    else:
                        ans.append(False)
        return ans

