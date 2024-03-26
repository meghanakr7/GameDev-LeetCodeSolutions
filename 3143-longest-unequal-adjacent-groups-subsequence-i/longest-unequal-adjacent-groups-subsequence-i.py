class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        if(len(groups) ==  1):
            return words 
        dp = [0]*len(groups)
        dp[0] = 0
        ind = []
        ind.append(0)
        for i in range(1, len(groups)):
            if(groups[i-1] != groups[i]):
                dp[i] = dp[i-1]+1
                ind.append(i)
            else:
                groups[i] = groups[i-1]
                dp[i] = dp[i-1]
        res = []
        for i in range(len(ind)):
            res.append(words[ind[i]])
        return res
        
            




        