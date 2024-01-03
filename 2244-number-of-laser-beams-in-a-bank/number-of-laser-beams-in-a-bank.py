class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n = len(bank)
        total = 0
        for i in range(n-1):
            j = i + 1
            icount = bank[i].count('1')
            if icount == 0:
                continue
            count = 0
            while j < n and not count:
                count = bank[j].count('1')
                j = j + 1
            total += icount * count
        return total

        