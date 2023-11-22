class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = []*len(strs)
        # print("inital d ",d)
        for i in range(len(strs)):
            temp = {}
            for char in strs[i]:
                if char in temp:
                    temp[char] += 1
                else:
                    temp[char] = 1
            temp = dict(sorted(temp.items()))
            d.append(temp)
        #     print("After first is ",d)
        # print("d is ",d)
        e = []
        indices = set()
        for i in range(len(d)):
            if i not in indices:
                temp = []
                temp.append(strs[i])
                indices.add(i)
                for j in range(i+1, len(d)):
                    if d[j] == d[i] and j not in indices:
                        temp.append(strs[j])
                        indices.add(j)
                e.append(temp)
        # print("E is ",e)
        return e

