class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        
        d = sorted(d.items(), key = lambda x: x[1],reverse = True)
        # print("d is ",d)
        newString = ""
        for key, val in d:
            while val:
                newString += key
                val -=1
        print("newString is ",newString)
        return newString
        