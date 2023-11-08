class Solution:
    # import Math
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        print("Actual time is ",(abs(sx - fx) + abs(sy - fy)))
        time = max(abs(sx - fx) , abs(sy - fy))
        # xdist = abs(sx-fx)**2
        # ydist = abs(sy-fy)**2
        # if (sx, sy) ==
        # print("xdist and ydist ",xdist, ydist)
        # time =  (xdist + ydist) ** 0.5
        
        print("dist is ",time, floor(time))
        if sx == fx and sy == fy:
            if t == 1:
                return False
        if floor(time) <= t:
            return True
        return False
        