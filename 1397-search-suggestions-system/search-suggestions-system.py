class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        finalres = []
        products.sort()
        v = set()
        for i in range(len(searchWord)):
            for s in products:
                if i < len(s) and s[i] == searchWord[i] and len(res) < 3 and s not in v:
                    res.append(s)
                if i < len(s) and s[i]!=searchWord[i]:
                    v.add(s)
            finalres.append(res)
            res = []
        return finalres

        