class Graph(object):
    def __init__(self):
        self.graph = {}
        self.color = {}
 
    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
 
    def set_color(self, u, color):
        self.color[u] = color
 
    def bfs(self, s):
        distance = 0
        color = self.color[s]
        visited = [0] * (len(self.graph)+1)
        queue = []
        queue.append(s)
        visited[s] = 1
        while queue:
            s = queue.pop(0)
            distance += 1
            for t in self.graph[s]:
                if not visited[t]:
                    if self.color[t] == color:
                        return distance
                    queue.append(t)
                    visited[t] = 1
        return 10**6
 
 
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = Graph()
    for u, v in zip(graph_from, graph_to):
        graph.add_edge(u, v)
        graph.add_edge(v, u)
    for u in range(1, len(ids)+1):
        graph.set_color(u, ids[u-1])
    min_distance = 10**6
    for u in range(1, graph_nodes+1):
        if graph.color[u] == val:
            min_distance = min(min_distance, graph.bfs(u))
    if min_distance == 10**6:
        return -1
    return min_distance

for ha in range(3):
    graph_nodes, graph_edges = map(int, input().split())
    edges = list(map(int, input().split()))
    graph_from = edges[::2]
    graph_to = edges[1::2]
    ids = list(map(int, input().rstrip().split()))
    val = int(input())
    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)
    print(ans,'\nnext one\n')

sample 0 :
4 3
1 2
1 3
4 2
1 2 3 4
2

output: -1

sample 1:
4 3
1 2
1 3
4 2
1 2 1 1 
1

output: 1

sample 2:
5 4
1 2
1 3
2 4
3 5
1 2 3 3 2
2


output:3