class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(numbers)):
            if((target - numbers[i]) in numbers[i+1:]):
                res.append(i + 1)
                res.append(numbers[i+1:].index(target - numbers[i]) + 2 + i)
                return res

        