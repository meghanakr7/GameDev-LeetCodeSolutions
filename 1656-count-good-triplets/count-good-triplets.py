class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        first = 0
        sec = 0
        count = 0
        third = 0
        for i in range(len(arr)):
            first = arr[i]
            for j in range(i+1, len(arr)):
                sec = arr[j]
                if(abs(first - sec) > a):
                    continue
                for k in range(j+1, len(arr)):
                    third = arr[k]
                    if(abs(sec - third) > b):
                        continue
                    if(abs(first - third) > c):
                        continue
                    else:
                        count += 1
        # print('count is ',count)
        return count
                    
                    

        