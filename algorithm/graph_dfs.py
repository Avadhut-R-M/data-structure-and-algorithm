from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,start,end):
        self.graph[start].append(end)

    def dfs(self,node,visited = {},out=[]):
        if not visited.get(node,None):
            out.append(node)
            visited[node] = True

        for nei in self.graph[node]:
            if not visited.get(nei,None):
                self.dfs(nei, visited, out)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 0)
g.add_edge(2, 4)
g.add_edge(0, 3)

visited = {}
out = []
g.dfs(0,visited,out)
print(out)

