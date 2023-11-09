class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        d = defaultdict()
        for i in range(len(queries)):
            d[i] = 0
            circle = queries[i]
            circle_center_x = circle[0]
            circle_center_y = circle[1]
            circle_radius = circle[2]
            for j in range(len(points)):
                x, y = points[j][0], points[j][1]
                dist = ( (circle[0] - x)**2 + (circle[1] - y)**2 )
                dist = dist**(0.5)
                if dist <= circle_radius:
                    d[i] += 1
        return list(d.values())



        