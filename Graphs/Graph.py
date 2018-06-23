class Vertex:
    def __init__(self, key):
        self.key = key
        self.connectedTo = {}

    def addNeighbour(self, neighbour, weight=0):
        self.connectedTo[neighbour] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, key):
        return self.connectedTo[key]

    def __str__(self):
        return "{} connected to: {}".format(self.key, [(k.key, w) for k, w in self.connectedTo.items()])


class Graph:
    "non-directional graph"

    def __init__(self):
        self.root = None
        self.vertices = {}

    def addVertex(self, key):
        newVertex = self.vertices[key] = Vertex(key)
        if not self.root:
            self.root = newVertex
        return newVertex

    def addEdge(self, a, b, weight=0):
        if a not in self.vertices:
            self.addVertex(a)
        if b not in self.vertices:
            self.addVertex(b)
        self.vertices[a].addNeighbour(self.vertices[b], weight)
        self.vertices[b].addNeighbour(self.vertices[a], weight)

    def bfs(self, start, goal):
        # return nothing if starting key doesnt exist
        if start not in self.vertices:
            return []

        # queue of vertices to check
        vertQueue = []
        vertQueue.insert(0, [self.vertices[start]])

        # set of explored vertices
        explored = set()

        while vertQueue:
            path = vertQueue.pop()
            curr = path[len(path) - 1]
            if curr.key == goal:
                return path
            for v in curr.getConnections():
                if v not in explored:
                    vertQueue.insert(0, path + [v])
            explored.add(curr)
        return []

    def getWeight(self, a, b):
        self.vertices[a].getWeight(b)

    def getVertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())


def test_bfs():
    g = Graph()
    g.addEdge(2, 3)
    g.addEdge(3, 2, 5)
    g.addEdge(5, 3)
    g.addEdge(3, 1, 6)
    g.addEdge(2, 8, 90)
    test_cases = [3, 4, 5, 6, 7, 2]
    expected = [[2, 3], [], [2, 3, 5], [], [], [2]]
    for i in range(len(test_cases)):
        result = g.bfs(g.root, test_cases[i])
        result = [v.key for v in result]
        status = 'PASS' if result == expected[i] else 'FAIL'
        print("{}. case: {}, expected: {}. got: {}".format(status,
                                                           test_cases[i], expected[i], result))


if __name__ == '__main__':
    test_bfs()
