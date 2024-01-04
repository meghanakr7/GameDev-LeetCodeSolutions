class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mini = min(nums)
        if mini > 0:
            return 1
        startVal =  1
        
        while True:
            false = 0
            prevVal = startVal
            for i in range(len(nums)):
                if(prevVal + nums[i] < 1):
                    startVal += 1
                    false = 1
                    break
                else:
                    prevVal = prevVal + nums[i]
            if not false:
                print('start is ',startVal)
                return startVal
        