from graph.graph import Graph, Vertex, Edge


# Node can be successfully added to the graph
def test_add_node_to_graph():
    graph = Graph()
    actual = graph.add_node('a').value
    expected = 'a'
    assert actual == expected


# An edge can be successfully added to the graph
def test_add_edge_to_graph():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.add_edge(a, b)
    assert True


# A collection of all nodes can be properly retrieved from the graph
def test_node_collection():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    actual = graph.get_nodes()
    assert actual == [a, b, c]


# All appropriate neighbors can be retrieved from the graph
def test_get_neighbors():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    e_1 = graph.add_edge(a, b, 2)
    e_2 = graph.add_edge(a, c, 2)
    actual = graph.get_neighbors(a)
    assert actual == [e_1, e_2]


def test_get_neighbors_none():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    actual = graph.get_neighbors(a)
    assert actual == []


# Neighbors are returned with the weight between nodes included
def test_get_neighbors_weight():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    e_1 = graph.add_edge(a, b, 3)
    e_2 = graph.add_edge(a, c, 4)
    neighbor_1 = graph.get_neighbors(a)[0]
    neighbor_2 = graph.get_neighbors(a)[1]
    assert neighbor_1.weight == 3 and neighbor_2.weight == 4


# The proper size is returned, representing the number of nodes in the graph
def test_graph_size():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    actual = graph.size()
    assert actual == 2


# A graph with only one node and edge can be properly returned
def test_one_node_one_edge():
    graph = Graph()
    a = graph.add_node('a')
    edge = graph.add_edge(a, a)
    actual = graph.get_neighbors(a)
    assert actual == [edge]


# An empty graph properly returns None
def test_empty_graph():
    graph = Graph()
    actual = graph.get_nodes()
    assert actual is None