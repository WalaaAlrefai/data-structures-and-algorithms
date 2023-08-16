from graph.graph import Graph,Vertex

def depth_first(self, start_vertex):
        """
        Depth first Methog for class Graph
        Arguments: Node (Starting point of search)
        Return: A collection of nodes in their pre-order depth-first traversal order
        Program output: Display the collection
        """
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
    # Usage example
    # graph = Graph()
    # vertex1 = graph.add_node(1)
    # vertex2 = graph.add_node(2)
    # graph.add_edge(vertex1, vertex2)
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