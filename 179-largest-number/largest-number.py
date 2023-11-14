class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strNums = []
        lst = []
        for i in range(len(nums)):
            lst += [str(nums[i])]
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if str(lst[i]) + str(lst[j]) > str(lst[j]) + str(lst[i]):
                    continue
                else:
                   lst[i], lst[j] = lst[j], lst[i]
        print("strNums ",lst)
        if int("".join(lst)) == 0:
            return "0"
        return "".join(lst)
