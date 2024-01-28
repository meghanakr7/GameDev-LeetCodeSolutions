class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        convArr = []
        maxi = nums[0]
        convArr.append(nums[0] + maxi)
        for i in range(1, len(nums)):
            maxi = max(maxi, nums[i])
            convArr.append(nums[i] + maxi)
        print('convArr is ',convArr)
        res = []
        res.append(convArr[0])
        for i in range(1, len(nums)):
            res.append(convArr[i] + res[-1])
        print('res is ', res)
        return res