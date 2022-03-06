from cmath import inf
from heapq import heapify, heappop, heappush
from collections import defaultdict
import queue

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, start, end, weight):
        self.graph[start].append((end, weight))
        self.graph[end].append((start, weight))

    def prims_algo(self, adj, n):
        queue = []
        key = [False] * n
        parents = [-1] * n
        weight = [float('inf')] * n
        for i in range(n):
            if key[i] == False:
                parents[i] = 0
                heappush(queue, (0, i, -1))
                while queue:
                    wei, node, parent = heappop(queue)
                    if key[node] == True:
                        pass
                    key[node] = True
                    if weight[node] > wei:
                        weight[node] = wei
                        parents[node] = parent
                    for nei, w in adj[node]:
                        if key[nei] != True:
                            heappush(queue, (w, nei, node))
        return parents

g = Graph()
g.add_edge(1, 5, 4)
g.add_edge(4, 5, 9)
g.add_edge(1, 4, 1)
g.add_edge(4, 3, 5)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(4, 3, 3)
g.add_edge(3, 6, 8)
g.add_edge(2, 6, 7)
print(g.prims_algo(g.graph, 7))
