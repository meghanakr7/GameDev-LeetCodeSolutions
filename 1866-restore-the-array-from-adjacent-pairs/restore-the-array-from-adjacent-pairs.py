class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        ap = adjacentPairs
        # ele = [element for row in ap for element in row]
        start = 0
        d = defaultdict(list)
        
        for i in ap:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        for i in d:
            if len(d[i]) == 1:
                start = i
                break
        nums = [start]
        stack = [d[start]]
        visited = set()
        visited.add(start)
        while stack:
            cur = stack.pop()
            for ele in cur:
                if ele not in visited:
                    nums.append(ele)
                    stack.append(d[ele])
                    visited.add(ele)
        return nums