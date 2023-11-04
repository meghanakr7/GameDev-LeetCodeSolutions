class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        maxi = -math.inf
        for i in range(len(left)):
            maxi = max(left[i], maxi)
        for j in range(len(right)):
            maxi = max(n -right[j], maxi)
        print("maxi is ",maxi)
        return maxi

            

        