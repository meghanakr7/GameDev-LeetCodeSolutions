class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 1
        allRes = []
        z = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                z += 1
            else:
                res *= nums[i]
        print('res is ',res)
        if z >1 :
            return [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] !=0:
                if z == 1:
                    allRes.append(0)
                else:
                    allRes.append(int(res / nums[i]))
            else:
                allRes.append(res)
        # print('allRees ',allRes)
        return allRes



        