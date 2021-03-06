# from queue import Queue
from data_structures_and_algorithms.graph.queue import *


class Node:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return self.value


class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """
         * Adds a new node to the graph.
         * Takes in the value of that node.
         * Returns the added node.
        """
        try:
            node = Node(value)
            self._adjacency_list[node.value] = []
            return node
        except Exception as error:
            print(f'An error occurred: {error}')        

    def add_edge(self, start_node, end_node, weight=1):
        """
           * Adds a new edge between two nodes in the graph.
           * Include the ability to have a “weight”.
           * Takes in the two nodes to be connected by the edge.
           * Both nodes should already be in the Graph.
        """
        try:
            if start_node not in self._adjacency_list or end_node not in self._adjacency_list:
                raise KeyError('Nodes are not in the graph')
            self._adjacency_list[start_node].append((end_node, weight))
            self._adjacency_list[end_node].append((start_node, weight))
        except Exception as error:
            print(f'An error occurred: {error}')

    def get_nodes(self):
        """
        Returns all of the vertexes in the graph as a collection.
        """
        try:
            return list(self._adjacency_list.keys())
        except Exception as error:
            print(f'An error occurred: {error}')   

    def get_neighbors(self, node):
        """
         * Returns a collection of edges connected to the given node.
         * Takes in a given node.
         * Include the weight of the connection in the returned collection.
        """
        try:
            return self._adjacency_list[node]
        except Exception as error:
            print(f'An error occurred: {error}')   

    def size(self):
        """
         Returns the total number of nodes in the graph.
        """
        try:
            return len(self._adjacency_list)
        except Exception as error:
            print(f'An error occurred: {error}')    

    
    def breadth_first(self, start_node):
        """
         Traverse the graph using breadth first approach.

         Arguments:
            start_node: A node in the graph to start traversing from.
            
         Output:
            A list containing all nodes in the graph.
        """
        
        # try:
        if start_node not in self._adjacency_list:
                raise KeyError('Nodes are not in the graph')

        q = Queue()
        q.enqueue(start_node)
        visited_nodes = {}
        visited_nodes[start_node] = True
        output = []

        while len(q):
            cur = q.dequeue()
            output.append(cur)
            neighbors = self._adjacency_list[cur]
            for n in neighbors:
                if n[0] not in visited_nodes:
                    q.enqueue(n[0]) 
                visited_nodes[n[0]] = True
        return output
        # except Exception as error:
        #     return(f'{error}')

if __name__ == "__main__":
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    
    g.add_edge('a','b',5)
    g.add_edge('b','c',5)
    g.add_edge('b','a',5)
    g.add_edge('c','a',5)

    print(g.breadth_first('c'))