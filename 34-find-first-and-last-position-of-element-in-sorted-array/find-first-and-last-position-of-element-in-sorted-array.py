class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        def findStart(nums):
            left = 0
            mid = 0
            right = len(nums) - 1
            found = 0
            while left < right:
                mid = left + (right - left)//2
                print("mid ",nums[mid],target)
                if nums[mid] == target and (mid == 0 or nums[mid-1] < target):
                    found = 1
                    break
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            print("mid is ",mid,found)
            if not found:
                if nums[0] == target:
                    return 0
                return -1
            return mid
        def findEnd(nums):
            left = 0
            mid = 0
            found = 0
            right = len(nums) - 1
            while left < right:
                mid = left + (right - left)//2
                if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] > target):
                    found = 1
                    break
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            print("mid is ",mid,found)
            if not found:
                if nums[len(nums)-1] == target:
                    return len(nums)-1
                return -1
            return mid
        left = findStart(nums)
        right = findEnd(nums)
        print("left and right are ",left, right)
        if left == -1 and right == -1:
            return [-1, -1]
        if left == -1:
            return [right, right]
        if right == -1:
            return [left, left]
        return [left, right]
