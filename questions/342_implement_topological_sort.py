from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def topological_sort_util(self, i, adj, visited, out):
        visited[i] = 1
        for nei in adj[i]:
            if not visited[nei]:
                self.topological_sort_util(nei, adj, visited, out)
        out.insert(0,i)

    def topological_sort(self, v, adj):
        visited = [0]*v
        out = []

        for i in range(v):
            if not visited[i]:
                self.topological_sort_util(i, adj, visited, out)
        return out

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(1, 3)
g.add_edge(0, 3)
print(g.topological_sort(5,g.graph))