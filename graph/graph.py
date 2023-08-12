class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight

    def __str__(self):
        return f"({self.vertex}, {self.weight})"


class Graph:
    def __init__(self):
        self._adj_list = {}

    def add_node(self, val):
        v = Vertex(val)
        self._adj_list[v] = []
        return v

    def add_edge(self, start, end, weight=1):
        if start not in self._adj_list:
            raise KeyError('Start vertex not in graph!')
        if end not in self._adj_list:
            raise KeyError('End vertex not in graph!')
        edge = Edge(end, weight)
        self._adj_list[start].append(edge)

        return edge

    def get_nodes(self):
        return list(self._adj_list) or None

    def get_neighbors(self, vertex):
        return self._adj_list[vertex]

    def size(self):
        return len(self._adj_list)

    def __str__(self):
        return str(self._adj_list)

    def breadth_first(self, vertex):
        nodes = []
        breadth = [vertex]
        visited = set()

        visited.add(vertex)

        while breadth:
            front = breadth.pop(0)
            nodes.append(front)

            for neighbor in self.get_neighbors(front):
                if neighbor.vertex not in visited:
                    visited.add(neighbor)
                    breadth.append(neighbor.vertex)

        return nodes


if __name__ == "__main__":
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    e_1 = graph.add_edge(a, b, 2)
    e_2 = graph.add_edge(a, c, 2)
    print(graph.get_nodes())