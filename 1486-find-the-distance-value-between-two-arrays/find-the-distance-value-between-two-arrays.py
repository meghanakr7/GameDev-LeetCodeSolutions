class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        enter = False
        for i in range(len(arr1)):
            enter = False
            for j in range(len(arr2)):
                if (abs(arr1[i] - arr2[j]) <= d):
                    enter = True
                    break
            if not enter:
                count += 1
            print('i is ',arr1[i])
        print('count is. ',count)
        return count
        