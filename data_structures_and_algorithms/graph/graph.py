class Node:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return self.value


class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        self._adjacency_list[node.value] = []

    def add_edge(self, start_node, end_node, weight=1):

        if start_node not in self._adjacency_list or end_node not in self._adjacency_list:
            raise KeyError('Nodes are not in the graph')
        

        
        self._adjacency_list[start_node].append((end_node, weight))
        self._adjacency_list[end_node].append((start_node, weight))

    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, node):
        return self._adjacency_list[node]


    def size(self):
        return len(self._adjacency_list)

if __name__ == "__main__":
    g = Graph()

    # Test add and get nodes
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    print(g.get_nodes())

    # Test size
    print(g.size())

    # Test add edge
    g.add_edge('a','b',2)
    g.add_edge('a','c',9)
    print(g.get_neighbors('a'))



  