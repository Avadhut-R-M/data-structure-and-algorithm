from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,start,end):
        self.graph[start].append(end)

    def color_node_util(self,i,adj,color,colored):
        if colored[i] == -1:
            colored[i] = color
            return all([self.color_node_util(nei,adj,1-color,colored) for nei in adj[i]])
        elif colored[i] != -1:
            return colored[i]==color

    def color_node(self,v,adj):
        colored = [-1]*v
        for i in range(v):
            if colored[i] == -1:
                if not self.color_node_util(i,adj,0,colored):
                    return False
        return True

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(1, 3)
g.add_edge(0, 3)
print(g.color_node(5,g.graph))