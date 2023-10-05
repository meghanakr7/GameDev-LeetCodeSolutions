class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        numsDup = []
        for i in range(len(nums)):
            numsDup.append(nums[i])
            numsDup.append(int(str(nums[i])[::-1]))
        # print("numsDup",numsDup)
        return len(set(numsDup))

