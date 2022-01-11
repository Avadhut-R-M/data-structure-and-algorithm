from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, start, end, weight):
        self.graph[start].append((end, weight))

    def topo_sort(self, adj, i, visited, out):
        visited[i] = 1
        for nei,weight in adj[i]:
            if visited[nei] == 0:
                self.topo_sort(adj, nei, visited, out)
        out.insert(0, i)
    
    def short_path(self, v, adj, start, end):
        visited = [0]*v
        out = []

        for i in range(v):
            if not visited[i]:
                self.topo_sort(adj, i, visited, out)

        distance = [99999] * v
        distance[start] = 0

        for i in out:
            for nei,weight in adj[i]:
                if distance[nei] > (weight + distance[i]):
                    distance[nei] =  weight + distance[i]
        return distance[end]

g = Graph()
g.add_edge(0, 1, 5)
g.add_edge(1, 2, 6)
g.add_edge(2, 4, 4)
g.add_edge(1, 3, 3)
g.add_edge(3, 4, 6)
print(g.short_path(5,g.graph,0,4))