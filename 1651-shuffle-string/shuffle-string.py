class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ['']*len(indices)

        for i in range(len(indices)):
            res[indices[i]] = s[i]
        print("res is ",res)
        return "".join(res)