class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        l = 0
        r = len(s)
        i = 0
        while l < r:
            if s[i] == 'I':
                res.append(l)
                l += 1
            if s[i] == 'D':
                res.append(r)
                r -= 1
            i += 1
            # print('l and r ',l,r)
        res.append(l)
        # print('res ',res, list(res))
        return res