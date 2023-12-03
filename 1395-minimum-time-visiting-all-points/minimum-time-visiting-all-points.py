class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def calcDist(point1, point2):
            return max(abs(point1[0]-point2[0]), abs(point1[1]-point2[1]))
        startPoint = points[0]
        dist = 0
        for i in range(1, len(points)):
            point = points[i]
            dist += calcDist(startPoint, point)
            startPoint = point
        return dist


        