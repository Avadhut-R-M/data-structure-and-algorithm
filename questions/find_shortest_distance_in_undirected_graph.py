from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)

    def shortest_distinace(self, adj, v, start, end):
        distance = [v+1]*v
        queue = []
        distance[start] = 0
        queue.append(start)

        while queue:
            node = queue.pop(0)
            for nei in adj[node]:
                if distance[node] + 1 < distance[nei]:
                    distance[nei] = distance[node] + 1
                    queue.append(nei)

        return distance[end]

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 4)
g.add_edge(0, 3)
print(g.shortest_distinace(g.graph,5,0,4))