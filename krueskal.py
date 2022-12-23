class Graph:

    def __init__(self, v):
        self.V = v
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, livel, x, y):

        if livel[x] < livel[y]:
            parent[x] = y
        elif livel[x] > livel[y]:
            parent[y] = x

        else:
            parent[y] = x
            livel[x] += 1

    def kurskalmst(self):

        result = []

        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        livel = []
        for node in range(self.V):
            parent.append(node)
            livel.append(0)

        while e < self.V - 1:

            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, livel, x, y)

        minCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minCost)


g = Graph(4)
g.addEdge(0, 2, 6)
g.addEdge(0, 1, 10)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.kurskalmst()
