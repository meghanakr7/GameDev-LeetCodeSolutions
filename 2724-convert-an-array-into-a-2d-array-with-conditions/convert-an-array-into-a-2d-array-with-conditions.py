class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        maxNum = 0
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = nums.count(nums[i])
            if maxNum < nums.count(nums[i]):
                maxNum = nums.count(nums[i])
        # print("count is ",count,maxNum)
        i = 1
        sol = []
        res = []
        while i <= maxNum:
            sol = []
            for j in count.keys():
                # print("val of j and i is ",j,i)
                if count[j] >= i:
                    sol.append(j)
            # print("Sol is ",sol)
            res.append(sol)
            i += 1
        # print("Res is ",res)
        return res
            


        # for i in range(len(count)):


        

        