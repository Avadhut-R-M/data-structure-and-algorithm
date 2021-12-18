from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,start,end):
        self.graph[start].append(end)

    def bfs(self, start):
        viisited = {}
        queue = []
        out =[]
        queue.append(start)
        viisited[start]=True

        while queue:
            node = queue.pop(0)
            out.append(node)

            for nei in self.graph[node]:
                if not viisited.get(nei,None):
                    queue.append(nei)
                    viisited[nei]=True
        return out

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 0)
g.add_edge(2, 4)
g.add_edge(0, 3)
print(g.bfs(0))

