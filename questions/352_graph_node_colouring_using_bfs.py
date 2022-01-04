from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,start,end):
        self.graph[start].append(end)

    def color_node_util(self,colored,i,adj,color):
        colored[i] = 0
        queue = []
        queue.append(i)

        while(queue):
            node = queue.pop(0)
            for nei in adj[node]:
                if colored[nei] == -1:
                    colored[nei] = 1- colored[node]
                    queue.append(nei)
                else:
                    if colored[nei] != 1 - colored[node]:
                        return False
        return True

    def color_node(self, v, adj):
        colored = [-1] * v
        dfs_visited = {}
        for i in range(v):
            if colored[i] == -1:
                if not self.color_node_util(colored,i,adj,0):
                    return False
        return True

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(1, 3)
g.add_edge(0, 3)
print(g.color_node(5,g.graph))