from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,start,end):
        self.graph[start].append(end)

    def detect_cycle_util(self,visited,i,parent,adj, dfs_visited):
        dfs_visited[i] = True
        visited[i]=True
        for nei in adj[i]:
            if nei != parent and dfs_visited.get(nei,None):
                return True
            if nei != parent and self.detect_cycle_util(visited,nei, i, adj, dfs_visited):
                return True
        dfs_visited[i] = False
        return False

    def detect_cycle(self, v, adj):
        visited = {}
        dfs_visited = {}
        for i in range(v):
            if not visited.get(i,None):
                if self.detect_cycle_util(visited,i,None,adj, dfs_visited):
                    return True
        return False

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 4)
g.add_edge(0, 3)
print(g.detect_cycle(5,g.graph))