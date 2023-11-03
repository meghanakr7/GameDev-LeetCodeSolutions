class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        ares = []
        print("first and last ",target[0],target[-1])
        for i in range(1,n+1):
            if i in target:
                res.append(1)
                if i == target[-1]:
                    break
            else:
                res.append(1)
                res.append(-1)
        for i in res:
            if i == 1:
                ares.append("Push")
            else:
                ares.append("Pop")
        return ares

        