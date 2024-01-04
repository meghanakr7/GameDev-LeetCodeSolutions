class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = {}
        totalCount = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        for key, val in d.items():
            if val == 1:
                return -1
            elif val % 3 == 0:
                totalCount += val // 3
            elif val == 2:
                totalCount += 1
            elif val == 4:
                totalCount += 2
            else:
                num = val
                while(num > 0 and (num%3 != 0 or (val - num) % 2 != 0)):
                    num -= 1
                totalCount += (num//3) + (val - num)//2
        return totalCount

        