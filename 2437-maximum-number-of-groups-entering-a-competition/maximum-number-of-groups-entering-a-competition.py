class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        left = 1
        right = len(grades)
        def feasible(mid):
            if (mid+1) * (mid+2) //2 > len(grades):
                return True
            return False
        while left < right:
            mid = left + (right - left)//2
            print("mid is  ",mid)
            if feasible(mid):
                right = mid
                print("Right is ",mid)
            else:
                left = mid + 1
                print("left is ",left)
        return left
        