class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map = [0]*128
        if len(t) > len(s):
            return ""
        for i in t:
            map[ord(i)] += 1
        count = len(t)
        start = 0
        end = 0
        startIndex = 0
        min_len = math.inf
        while end < len(s):
            if map[ord(s[end])] > 0:
                count -= 1
            map[ord(s[end])] -= 1
            end += 1
            print('cout ',count)
            while count == 0:
                if end - start < min_len:
                    startIndex = start
                    min_len = end - start
                if(map[ord(s[start])] == 0):
                    count += 1
                map[ord(s[start])] += 1
                start +=1
        return "" if min_len == math.inf else s[startIndex : startIndex+min_len]

            
        
