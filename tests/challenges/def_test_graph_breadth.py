import sys
sys.path.insert(1, '/home/dana/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms.challenges.depth_first.depth_first import *
import pytest 

def test_depth_first(prepare_graph):
    graph = prepare_graph
    assert depth_first(graph._adjacency_list) == ['a', 'b', 'c', 'g', 'd', 'e', 'h', 'f']

def test_depth_first_for_empty_graph():
    graph = Graph()
    with pytest.raises(ValueError):
         depth_first(graph._adjacency_list) 


def test_another_case():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    
    g.add_edge('a','b',5)
    g.add_edge('b','c',2)
    g.add_edge('b','a',9)
    g.add_edge('c','a',5)
    assert depth_first(g._adjacency_list) == ['a', 'b', 'c']


@pytest.fixture
def prepare_graph():

    graph = Graph()

    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_node('e')
    graph.add_node('f')
    graph.add_node('g')
    graph.add_node('h')

    graph.add_edge('a', 'b')
    graph.add_edge('a', 'd')

    graph.add_edge('b', 'c')
    graph.add_edge('b', 'd')

    graph.add_edge('c', 'g')

    graph.add_edge('d', 'e')
    graph.add_edge('d', 'h')
    graph.add_edge('d', 'f')

    graph.add_edge('f', 'h')

    return graph