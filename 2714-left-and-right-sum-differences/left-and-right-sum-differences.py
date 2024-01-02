class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftArr = []
        rightArr = []
        leftSum = 0
        rightSum = 0
        res = []
        for i in range(len(nums)):
            leftArr.append(leftSum)
            leftSum += nums[i]
        for i in range(len(nums)-1,-1, -1):
            rightArr.append(rightSum)
            rightSum += nums[i]
        rightArr = rightArr[::-1]
        print(leftArr, rightArr)
        for i in range(len(leftArr)):
            res.append(abs(leftArr[i] - rightArr[i]))
        print('res is ',res)
        return res