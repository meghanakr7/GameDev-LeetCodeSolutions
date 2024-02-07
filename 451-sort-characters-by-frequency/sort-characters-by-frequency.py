class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        d = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))
        res = ''
        items = list(d.keys())
        for i in range(len(d.items())):
            val = d[items[i]]
            while(val):
                res += items[i]
                val -= 1
        return res


        
        