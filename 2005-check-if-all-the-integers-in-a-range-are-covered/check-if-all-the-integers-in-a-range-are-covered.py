class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        allNums = set()
        m = len(ranges)
        n = len(ranges[0])
        for i in range(m):
            for j in range(ranges[i][0], ranges[i][1] + 1):
                allNums.add(j)
        print('allNums are ',allNums)
        for i in range(left, right+1):
            if i not in allNums:
                return False
        return True

        
        