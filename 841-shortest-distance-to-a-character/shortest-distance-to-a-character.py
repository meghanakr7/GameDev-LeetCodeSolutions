class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        allIndices = []
        for i in range(len(s)):
            if s[i] == c:
                allIndices.append(i)
        print('allIndices are ',allIndices)
        minR = []
        start = 10001
        end = 10001
        k = 0
        if(len(allIndices) > 1):
            start = allIndices[0]
            end = allIndices[1]
            k = 2
            print('start end ',start,end)
        if(len(allIndices) == 1):
            start = allIndices[0]
        for i in range(len(s)):
            print('start, end in inf ',start,end,i)
            minR.append(min(abs(start-i), abs(end -i)))

            if i >= end:
                start = end
                if k < len(allIndices):
                    end = allIndices[k]
                k +=1
        print('minR ',minR)
        return minR


        