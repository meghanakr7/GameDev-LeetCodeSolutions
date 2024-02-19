class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        numbers.sort()
        while i < j:
            if(numbers[i] + numbers[j] == target):
                return [i+1, j+1]
            elif(numbers[i] + numbers[j] > target):
                j -= 1
            else:
                i += 1
        print('i and j are ',i,j)

        