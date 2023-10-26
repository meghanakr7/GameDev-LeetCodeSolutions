class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        l = set()
        if finalSum%2 != 0:
            return l
        else:
            s = 0
            i = 2
            while s < finalSum:
                s += i
                l.add(i)
                i += 2
                if s == finalSum:
                    return l
                if s > finalSum:
                    l.discard(s - finalSum)
                    return l
        return
                