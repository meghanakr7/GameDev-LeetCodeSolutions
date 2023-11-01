class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        appropriate_weight = 0
        def feasible(mid):
            d = 0
            i = 0
            computed_weight = 0
            while i < len(weights):
                s = 0
                while i < len(weights) and s + weights[i]<= mid:
                    s += weights[i]
                    computed_weight += weights[i]
                    i += 1
                print("s value for day is ",s)
                d += 1
            print("i and d are ",i,d,computed_weight)
            if computed_weight == sum(weights) and d <= days:
                return True
            return False
        while left < right:
            appropriate_weight = left + (right - left)//2
            print("approporate weight is ",left, right, appropriate_weight)
            if feasible(appropriate_weight):
                right = appropriate_weight
            else:
                left = appropriate_weight + 1
            # print("mid, left, right",appropriate_weight, left,right)
        return left
        
            

        