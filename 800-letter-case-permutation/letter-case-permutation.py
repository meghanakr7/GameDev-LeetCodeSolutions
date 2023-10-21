class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def dfs(ind, s):
            for i in range(ind, len(s)):
                if s[i].isalpha():
                    if s[i].isupper():
                        s1 = s[:i] + s[i].lower() + s[i+1:]
                    else:
                        s1 = s[:i] + s[i].upper() + s[i+1:]
                    res.append(s1)
                    dfs(i+1, s1)
                else:
                    continue

        dfs(0,s)
        res.append(s)
        # print("Res is ",res)
        return res