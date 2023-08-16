from graph.graph import Graph
from graph_depth_first.graph_depth_first import depth_first
import pytest

def test_depth_first(nodes):

    graph, a, b, c, d, e, f, g, h = nodes
    
    traversal_result = graph.depth_first(a)
    expected_result = [a, b, c, g, d, e, h, f]
    
    assert [vertex.value for vertex in traversal_result] == [vertex.value for vertex in expected_result]

    # Displaying the result as a comma-separated string
    result_string = ', '.join([vertex.value for vertex in traversal_result])
    print("Depth-First Traversal Result:", result_string)

def test_depth_first_from_half_of_graph(nodes):
    graph, a, b, c, d, e, f, g, h = nodes 

    traversal_result = graph.depth_first(d)
    expected_result = [d, e, h, f]
    
    assert [vertex.value for vertex in traversal_result] == [vertex.value for vertex in expected_result]

    # Displaying the result as a comma-separated string
    result_string = ', '.join([vertex.value for vertex in traversal_result])
    print("Depth-First Traversal Result:", result_string)

@pytest.fixture
def nodes():
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
    
    return [graph, a, b, c, d,e,f,g,h]