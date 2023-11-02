class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(threshold):
            count = 0
            total = 0
            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count += 1
                if count >= k:
                    print("coutn is ",count)
                    return False
            print("Returing true with count ",count)
            return True
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = left + (right - left)//2
            print("left, mid, right ",left,mid,right)
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left


        