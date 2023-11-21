class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        revNums = []
        nums.sort()
        for i in range(len(nums)):
            revNums.append(int(str(nums[i])[::-1]))
        # print("revNums are ",revNums)
        diff = []
        for i in range(len(nums)):
            diff.append(revNums[i] - nums[i])
        # print("diff is ",diff)
        count = {}
        for i in range(len(diff)):
            if diff[i] in count:
                count[diff[i]] += 1
            else:
                count[diff[i]] = 1
        # print("Count is ",count)
        # print("count.keys ",count.keys())
        finalRes = 0
        for key in count.keys():
            val = count[key]
            finalRes += math.comb(val, 2)
        # print("finalres is ",finalRes)
        return finalRes % ((10**9)+7)
        
            