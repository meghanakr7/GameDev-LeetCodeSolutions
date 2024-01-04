class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = 0
        prevHeight = 0
        for i in range(len(gain)):
            localHeight = prevHeight + gain[i]
            maxi = max(localHeight, maxi)
            prevHeight = localHeight
        # print('maxi is ',maxi)
        return maxi
        