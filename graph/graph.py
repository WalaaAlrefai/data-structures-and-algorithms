class Vertex:
    def __init__(self, value):
        self.value = value
        self.visited = False  # Add a visited attribute

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
        """
        Arguments: value
        Returns: The added vertex
        Add a vertex to the graph

        """
        v = Vertex(val)
        self._adj_list[v] = []
        return v

    def add_edge(self, start, end, weight=1):
        """
        Arguments: 2 vertices to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two vertices in the graph
        If specified, assign a weight to the edge
        Both vertices should already be in the Graph
        """
        
        if start not in self._adj_list:
            raise KeyError('Start vertex not in graph!')
        if end not in self._adj_list:
            raise KeyError('End vertex not in graph!')
        edge = Edge(end, weight)
        self._adj_list[start].append(edge)

        return edge

    def get_nodes(self):
        """
        Arguments: none
        Returns all of the vertices in the graph as a collection (set, list, or similar)
        Empty collection returned if there are no vertices
        """
        return list(self._adj_list) or None

    def get_neighbors(self, vertex):
        """
        Arguments: vertex
        Returns a collection of edges connected to the given vertex
        Include the weight of the connection in the returned collection
        Empty collection returned if there are no vertices
        """
        return self._adj_list[vertex]

    def size(self):
        """
        Arguments: none
        Returns the total number of vertices in the graph
        0 if there are none
        """
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
    
    def depth_first(self, start_vertex):
        def dfs_recursive(vertex):
            result.append(vertex)
            vertex.visited = True
            for edge in self.get_neighbors(vertex):
                neighbor = edge.vertex
                if not neighbor.visited:
                    dfs_recursive(neighbor)
        
        result = []
        dfs_recursive(start_vertex)
        
        return result



if __name__ == "__main__":
    graph = Graph()
    a = graph.add_node("A")
    b = graph.add_node("B")
    c = graph.add_node("C")
    d = graph.add_node("D")
    e = graph.add_node("E")
    f = graph.add_node("F")
    g = graph.add_node("G")
    h = graph.add_node("H")
    graph.add_edge(a, b,2)
    graph.add_edge(b, c,2)
    graph.add_edge(c, g,2)
    graph.add_edge(a,d,2)
    graph.add_edge(b,d,2)
    graph.add_edge(d, e,2)
    graph.add_edge(d, h,2)
    graph.add_edge(d,f,2)
    graph.add_edge(h, f,2)

    start_vertex = d
    traversal_result = graph.depth_first(start_vertex)
    print("Depth-First Traversal Result:")
    for vertex in traversal_result:
        print(vertex.value, end=' ')
    
    # Usage example
    # graph = Graph()
    # vertex1 = graph.add_node(1)
    # vertex2 = graph.add_node(2)
    # graph.add_edge(vertex1, vertex2)

    # start_vertex = vertex1
    # traversal_result = graph.depth_first(start_vertex)
    # print("Depth-First Traversal Result:")
    # for vertex in traversal_result:
    #     print(vertex.value, end=' ')
    # graph = Graph()
    # a = graph.add_node('a')
    # b = graph.add_node('b')
    # c = graph.add_node('c')
    # e_1 = graph.add_edge(a, b, 2)
    # e_2 = graph.add_edge(a, c, 2)
    # print(graph.get_nodes())

    # # Creating a sample graph
    # graph = Graph()
    # node1 = graph.add_node(1)
    # node2 = graph.add_node(2)
    # node3 = graph.add_node(3)
    # node4 = graph.add_node(4)

    # # graph.add_node(node1)
    # # graph.add_node(node2)
    # # graph.add_node(node3)
    # # graph.add_node(node4)

    # e1= graph.add_edge(node1, node2)
    # e2=graph.add_edge(node1, node3)
    # e3=graph.add_edge(node2, node4)
    # print(graph.get_nodes())
    

