class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.N = n
        adj_list = defaultdict(list)
        for edge in edges:
            u, v, w = edge
            # print("Edge is ",edge)
            adj_list[u].append((v, w))
        # print("Adj ",adj_list)
        self.adj_list = adj_list
       
    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        
        self.adj_list[u].append((v, w))
    def shortestPath(self, node1: int, node2: int) -> int:
        priorityQueue = [(0, node1)]
        distances = [math.inf]*self.N
        distances[node1] = 0
        while priorityQueue:
            currentCost, currentNode = heapq.heappop(priorityQueue)
            if currentCost > distances[currentNode]:
                continue
            
            if currentNode == node2:
                return currentCost
            
            # print("Adj of current node ",self.adj_list[currentNode])
            for edge in self.adj_list[currentNode]:
                neighbor, cost = edge 
                costNow = cost + distances[currentNode]
                if distances[neighbor]  > costNow:
                    distances[neighbor] = costNow
                    heapq.heappush(priorityQueue, (costNow, neighbor))
        return -1 if distances[node2] == math.inf else  distances[node2]
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)