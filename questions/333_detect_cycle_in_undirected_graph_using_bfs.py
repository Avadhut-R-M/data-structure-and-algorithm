from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,start,end):
        self.graph[start].append(end)

    def detect_cycle(self):
        visited = {}
        queue = []
        first_key = list(self.graph.keys())[0]
        queue.append((None,first_key))
        visited[first_key]=True

        while queue:
            node = queue.pop(0)
            for nei in self.graph[node[1]]:
                if nei != node[0] and visited.get(nei,None):
                    return True
                if not visited.get(nei,None):
                    queue.append((node[1],nei))
        return False

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 4)
g.add_edge(0, 3)
print(g.detect_cycle())

