class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]] = 0
            d[arr[i]] += 1
        d = dict(sorted(d.items(), key = lambda x:x[1]))
        print('d is ',d)
        i = 0
        print('d keys ',d.keys())
        keys = list(d.keys())
        print(keys)
        count = 0
        print('keys are ',keys)
        while k:
            if k >= d[keys[i]]:
                k -= d[keys[i]]
                count += 1
            else:
                break
            i += 1
        print('count is ',count,len(keys)-count)
        return len(keys) - count

