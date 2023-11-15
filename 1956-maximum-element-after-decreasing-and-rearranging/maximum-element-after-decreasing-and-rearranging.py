class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        if 1 not in arr:
            arr.remove(max(arr))
            arr.append(1)
        arr.append(1)
        arr.sort()
        diff = 0
        for i in range(1, len(arr)):
            if(abs(arr[i] - arr[i-1])) <= 1:
                continue
            else:
                diff += abs(arr[i] - i)
                arr[i] = arr[i-1] + 1
        print("arr is ",arr)
        print("diff is ",diff)
        return max(arr)



        