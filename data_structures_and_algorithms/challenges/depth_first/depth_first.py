import sys
sys.path.insert(1, '/home/dana/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms.graph.graph import *


def depth_first(adjacent_list):
    """
    Implements a depth-first traversal on a graph.

    Arguments:
        Input: adjacency list as a graph.

        Output: list of nodes in their pre-order depth-first traversal order.
    """
    # try:
    if adjacent_list:
        all_nodes = list(adjacent_list.keys())

        output = []
        visited = set()

        output.append(all_nodes[0])
        visited.add(all_nodes[0]) 

        def _walkthrough(node):

            for neighbor in adjacent_list[node]:
                
                if neighbor[0] not in visited:
                    visited.add(neighbor[0]) 
                    output.append(neighbor[0])
                    _walkthrough(neighbor[0])

        _walkthrough(all_nodes[0])
        return output
    else:
        raise ValueError('Graph is empty')

    # except Exception as error:
    #     return f'An error occurred: {error}'



if __name__ == "__main__":

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

    print(depth_first(graph._adjacency_list))










