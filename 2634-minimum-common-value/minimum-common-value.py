class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        mini = math.inf
        for i in range(len(nums1)):
            high = len(nums2)-1
            low = 0
            while(low <= high):
                mid = low + (high-low)//2
                # print("mid ",mid, low,i)
                if nums2[mid] == nums1[i]:
                    return nums2[mid]
                elif nums2[mid] < nums1[i]:
                    low = mid + 1
                elif nums2[mid] > nums1[i]:
                    high = mid - 1
        if mini == math.inf:
            return -1
        return mini
        