from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,start,end):
        self.graph[start].append(end)

    def add_weighted_edge(self,start,end,weight):
        self.graph[start].append((end, weight))

g = Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
print(g.graph)
