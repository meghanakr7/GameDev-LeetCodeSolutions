class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        def isFeasible(mid):
            d = 1
            s = 0
            for i in range(len(weights)):
                if s + weights[i] <= mid:
                    s += weights[i]
                else:
                    s  = weights[i]
                    d += 1
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
