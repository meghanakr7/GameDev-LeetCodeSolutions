class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        kid = 0
        # print('g ',g,s)
        for i in range(len(g)):
            while kid <len(s) and s[kid] < g[i]:
                kid +=1
            if kid < len(s) and g[i]<=s[kid]:
                count += 1
            kid += 1
        # print('count is ',count)
        return count


        