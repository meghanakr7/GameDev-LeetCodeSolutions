class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        finalRes = []
        def arithmetic(sortedNums):
            total = sum(sortedNums)
            a = sortedNums[0]
            if len(sortedNums) == 1:
                return True
            # d = sortedNums[1] - sortedNums[0]
            # n = len(sortedNums)
            # # print("n is ",n, a, d)
            # sortedTotal = (n/2)*((2*a) + (n-1)*d)
            # print("sorted Total and total is ",sortedTotal, float(total))
            # if float(total) == sortedTotal:
            #     return True
            # return False
            for j in range(1, len(sortedNums)):
                if sortedNums[1] - sortedNums[0] != sortedNums[j] - sortedNums[j-1]:
                    return False
            return True
        for i in range(len(l)):
            if l[i]>r[i]:
                finalRes.append(False)
                continue
            sortedNums = sorted(nums[l[i]:r[i]+1])
            # print("sortedNums are ",sortedNums)
            if arithmetic(sortedNums):
                finalRes.append(True)
            else:
                finalRes.append(False)
        # print("FinalRes is ",finalRes)
        return finalRes
