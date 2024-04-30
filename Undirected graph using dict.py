class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def addEdge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def removeEdge(self, v1, v2):
        if v1 in self.graph[v2]:
            self.graph[v2].remove(v1)
        if v2 in self.graph[v1]:
            self.graph[v1].remove(v2)

    def removeVertex(self, v):
        if v in self.graph:
            del self.graph[v]
        for key, value in self.graph.items():
            if v in value:
                value.remove(v)

    # def depthFirst(self, start, visited = set()):
    #     if start not in visited:
    #         visited.add(start)
    #         print(start, end=" ")
    #         for vertex in self.graph[start]:
    #             self.depthFirst(vertex)

    def depthFirst(self, start):
        visited = {start}
        stack = [start]
        while len(stack) > 0:
            current = stack.pop()
            print(current)
            for vertex in self.graph[current]:
                if vertex not in visited:
                    stack.append(vertex)
                    visited.add(vertex)

    def breadthFirst(self, start):
        visited = {start}
        queue = [start]
        while len(queue) > 0:
            current = queue.pop(0)
            print(current)
            for vertex in self.graph[current]:
                if vertex not in visited:
                    queue.append(vertex)
                    visited.add(vertex)

    def display(self):
        for vertex, j in self.graph.items():
            print("Vertex: ", vertex, "==>", j)


g = Graph()
a = [0, 1, 2, 3, 4]
for i in a:
    g.addVertex(i)
# g.display()
edge = int(input("Enter number of edges: "))
for i in range(edge):
    x = list(map(int, input("Enter two vertices: ").split()))
    g.addEdge(x[0], x[1])
# g.display()
# g.removeEdge(2, 3)
# g.display()
print()
# g.removeVertex(3)
g.display()
g.breadthFirst(1)
# g.depthFirst(1)
