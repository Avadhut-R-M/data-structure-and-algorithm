from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def detect_cycle(self, v, adj):
        queue = []
        indegree = [0]*v
        out = []

        for i in adj:
            for k in adj[i]:
                indegree[k] += 1

        for i in range(v):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.pop(0)
            out.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return False if len(out) == v else True

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 4)
g.add_edge(0, 3)
print(g.detect_cycle(5,g.graph))