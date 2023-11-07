class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        monsters = 0
        n = len(dist)
        time = [0] * n
        monsters = 0
        for i in range(len(dist)):
            time[i] = dist[i] / speed[i]
        time = sorted(time)
        for i in range(len(time)):
            if time[i] <= i:
                break
            monsters += 1
        return monsters