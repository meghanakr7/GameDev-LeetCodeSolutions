class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, cur):
            if len(cur) > 2*n:
                return 
            if len(cur) == 2*n:
                res.append(cur)
            if left < n:
                dfs(left+1, right, cur + '(')
            if right < left:
                dfs(left, right + 1, cur + ')')
        dfs(0,0,'')
        print("res is ",res)
        return res