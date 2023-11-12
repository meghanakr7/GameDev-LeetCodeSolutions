class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        max_stop = max(max(route) for route in routes)
        if target > max_stop:
            return -1
        flag = True
        min_buses_to_reach = [math.inf] * (max_stop + 1)
        min_buses_to_reach[source] = 0
        while flag:
            flag = False
            for route in routes:
                mini = math.inf
                for stop in route:
                    mini = min(mini, min_buses_to_reach[stop])
                mini += 1
                for stop in route:
                    if min_buses_to_reach[stop] > mini:
                        min_buses_to_reach[stop] = mini
                        flag = True
        return min_buses_to_reach[target] if min_buses_to_reach[target] < math.inf else -1
