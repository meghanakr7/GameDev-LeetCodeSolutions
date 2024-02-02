class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pnum = []
        nnum = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                pnum.append(nums[i])
            else:
                nnum.append(nums[i])
        pindex = 0
        nindex = 0
        i = 0
        res = []
        # print('pnum is ',pnum, nnum)
        while i < len(nums):
            # print('pindex is ',pindex)
            if pindex < len(pnum):
                res.append(pnum[pindex])
            if nindex < len(nnum):
                res.append(nnum[nindex])
            pindex += 1
            nindex += 1
            i += 1
        return res

        