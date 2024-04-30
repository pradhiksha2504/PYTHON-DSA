from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph= defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def cyclicUtil(self, v, visited, recStack):
        visited[v] = 1
        recStack[v] =1
        for node in self.graph[v]:
            if visited[node] == 0:
                if self.cyclicUtil(node, visited, recStack):
                    return 1
            elif recStack[node] == 0:
                return 1
        recStack[v] = False
        return 0



    def isCyclic(self):
        visited = [0] * self.V
        recStack = [0] * self.V
        for node in range(self.V):
            if visited[node] == 0:
                if self.cyclicUtil(node, visited, recStack):
                    return True


    def dfs(self, start):
        visited = {start}
        stack = [start]
        while len(stack) > 0:
            current = stack.pop()
            print(current, end=" ")
            for v in self.graph[current]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)

    def display(self):
        print(self.graph)


g = Graph(4)
a = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 2], [3, 1]]
for i in a:
    g.addEdge(i[0], i[1])
g.dfs(0)
print()
g.display()
res = g.isCyclic()
print(res)