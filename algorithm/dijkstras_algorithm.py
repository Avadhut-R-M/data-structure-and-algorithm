from heapq import heapify, heappop, heappush
from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, start, end, weight):
        self.graph[start].append((end, weight))
        self.graph[end].append((start, weight))

    def dijkstras_short_path(self, adj, nodes, start, end):
        distance = [999999] * nodes
        priority_queue = []

        distance[start] = 0
        heappush(priority_queue,(0, start))
        
        while(priority_queue):
            weight, node = heappop(priority_queue)
            for nei, nei_weight in adj[node]:
                if distance[nei] > nei_weight + weight:
                    distance[nei] = nei_weight + weight
                    heappush(priority_queue, (distance[nei], nei))

        return distance[end]


g = Graph()
g.add_edge(0, 1, 5)
g.add_edge(1, 2, 6)
g.add_edge(2, 4, 4)
g.add_edge(1, 3, 3)
g.add_edge(3, 4, 10)
g.add_edge(0, 4, 1)
print(g.dijkstras_short_path(g.graph, 5, 0, 4))