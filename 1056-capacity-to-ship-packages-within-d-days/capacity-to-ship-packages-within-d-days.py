class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        def isFeasible(mid):
            d = 1
            s = 0
            # print("mid is ",mid)
            for i in range(len(weights)):
                if s + weights[i] <= mid:
                    s += weights[i]
                    # print("weights and s is ",weights[i],s)
                else:
                    print("till now s is ",s)
                    s  = weights[i]
                    d += 1
            # print("d is ",d)
            if d <= days:
                return True
            return False
        while left < right:
            mid = left + (right - left) // 2
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
