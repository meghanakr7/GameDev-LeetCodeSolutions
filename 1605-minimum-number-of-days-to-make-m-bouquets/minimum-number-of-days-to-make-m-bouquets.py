class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left = 1
        right = max(bloomDay)
        def feasible(mid):
            flowers = 0
            bouqets = 0
            for i in range(len(bloomDay)):
                # print("bloomDay and mid ", bloomDay[i],mid)
                if bloomDay[i] <= mid:
                    bouqets += (flowers+ 1)// k
                    flowers = (flowers + 1)%k
                    
                else:
                    flowers = 0
            #     print("at each steps ",flowers, bouqets)
            # print("bouqets and flowers are ",bouqets)
            if bouqets >= m:
                return True
            return False

        while left < right:
            mid = left + (right - left) // 2
            # print("left, mid, right ",left, mid, right)
            if feasible(mid):
                right = mid
                # print("Am i at right ",left, mid, right)
            else:
                
                left = mid + 1
                # print("last one is false ",left,mid,right)
            
        return left