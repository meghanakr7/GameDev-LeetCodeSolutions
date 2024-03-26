class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        print("len of groups ",groups, len(groups))
        if(len(groups) ==  1):
            return words
        
        dp = [0]*len(groups)
        dp[0] = 0
        ind = []
        ind.append(0)
        print("dp in early stages ",dp)
        for i in range(1, len(groups)):
            print("i-1, i ",groups[i-1],groups[i],i)
            if(groups[i-1] != groups[i]):
                dp[i] = dp[i-1]+1
                ind.append(i)
            else:
                groups[i] = groups[i-1]
                dp[i] = dp[i-1]
        print("inds are. ",ind)
        res = []
        print("words ae ",words)
        for i in range(len(ind)):
            res.append(words[ind[i]])
        print("res is ",res)
        return res
        
            




        