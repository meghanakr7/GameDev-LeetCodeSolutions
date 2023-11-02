class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
       
        print("initial left and right are ",left, right)
        def feasible(mid):
            hours = 0
            s = 0
            for pile in piles:
                s += math.ceil(pile/mid)
            if s > h:
                return False
            print("returning true bcoz of these many hrs ",hours)
            return True
        while left < right:
            mid = left + (right-left)//2
            print("left, mid, right ",left,mid,right)
            if feasible(mid):
                right = mid
                print("moving to right ",left,mid, right)
            else:
                left = mid + 1
                print("moving to left ",left,mid,right)
        return left
        