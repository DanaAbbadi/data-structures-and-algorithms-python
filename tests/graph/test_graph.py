from data_structures_and_algorithms.graph.graph import *
import pytest

def test_add_to_graph():
    g = Graph()
    g.add_node('a')
    g.add_node('b')

    assert list(g._adjacency_list.keys()) == ['a', 'b']

def test_add_edge():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')

    g.add_edge('a' , 'b' , 2)
    g.add_edge('a' , 'c' , 9)

    assert g._adjacency_list['a'][0] == ('b' , 2)
    assert g._adjacency_list['a'][0][0] == 'b'
    assert g._adjacency_list['a'][0][1] == 2

    assert g._adjacency_list['a'][1] == ('c' , 9)
    assert g._adjacency_list['a'][1][0] == 'c'
    assert g._adjacency_list['a'][1][1] == 9


def test_retrieve_nodes():
    g = Graph()
    g.add_node('a')
    g.add_node('b')

    assert g.get_nodes() == ['a', 'b']

def test_retrieve_neighbors():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')

    g.add_edge('a' , 'b' , 2)
    g.add_edge('a' , 'c' , 9)

    assert g.get_neighbors('a') == [('b' , 2) , ('c' , 9)]

def test_graph_size():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    assert g.size() == 2

def test_one_node_no_edges():
    g = Graph()
    g.add_node('a')
    assert g.get_neighbors('a') == []

def test_empty_graph():
    g = Graph()
    assert g.get_nodes() == []

def test_breadth_first():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    
    g.add_edge('a','b',5)
    g.add_edge('b','c',2)
    g.add_edge('b','a',9)
    g.add_edge('c','a',5)

    assert g.breadth_first('a') == ['a','b','c']

def test_breadth_first_not_in_graph():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')

    with pytest.raises(Exception):
        g.breadth_first('d')  

def test_breadth_first_start_from_end():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    
    g.add_edge('a','b',5)
    g.add_edge('b','c',1)
    g.add_edge('b','a',6)
    g.add_edge('c','a',9)

    assert g.breadth_first('c') == ['c','b','a']