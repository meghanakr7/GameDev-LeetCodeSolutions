class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.N = n
        self.INF = math.inf
        adj_list = defaultdict(list)
        for u, v, wt in edges:
            adj_list[u].append((v, wt))
        self.adj_list = adj_list
        
    def addEdge(self, edge: List[int]) -> None:
        print("Edge is ",edge)
        u,v,w = edge 
        self.adj_list[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = [math.inf] * self.N
        distances[node1] = 0

        priorityQueue = [(0, node1)]
        while priorityQueue:
            currentCost, currentNode = heapq.heappop(priorityQueue)
            print("Current cost and current node ",currentCost, currentNode)
            if currentCost > distances[currentNode]:
                continue
            
            if currentNode == node2:
                return currentCost
            
            for edge in self.adj_list[currentNode]:
                neighbor, edgeLength = edge
                newRouteCost = edgeLength + distances[currentNode]

                if distances[neighbor] > newRouteCost:
                    distances[neighbor] = newRouteCost
                    heapq.heappush(priorityQueue, (newRouteCost, neighbor))

        return -1 if distances[node2] == math.inf else distances[node2]


       

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)