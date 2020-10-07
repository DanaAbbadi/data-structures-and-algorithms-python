import sys
sys.path.insert(1, '/home/dana/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms.graph.graph import *

def list_to_dict(list_of_cities):
    """
     Convert the list of neighboors for a node to a dictionary, 
     to have better performance in terms of time complexity.

     Arguments:
        Input:
            list_of_cities : {list} a list of all cities with direct connection for a node/city
        Output:
            A dictionary of all cities with direct connection with their cost as a value.

    """
    output = {}
    for city in list_of_cities:
        output[city[0]] = city[1]
    return output

def get_direct_trips(graph, cities):
    """
     Return whether a full trip is possible with direct flights, and how much it would cost.

     Arguments:
        Input:
            graph  : {Graph} a graph where nodes/vertices represent cities with direct connectins.
            cities : {list}  an array of city names.
        Output:
            A string consisting of a booleon indicating if the trip is possible along with the cost.
    """
    cost = 0
    for city in range(len(cities)-1):
        direct_path = list_to_dict(graph.get_neighbors(cities[city]))
        if cities[city+1] not in direct_path:
            return 'False, $0'
        cost += direct_path[cities[city+1]]
    return f'True, ${cost}'


if __name__ == "__main__":
    cities_graph = Graph()

    cities_graph.add_node("Pandora")
    cities_graph.add_node("Metroville")
    cities_graph.add_node("Arendelle")
    cities_graph.add_node("Monstropolis")
    cities_graph.add_node("Narnia")
    cities_graph.add_node("Naboo")

    cities_graph.add_edge('Pandora', 'Arendelle', 150)
    cities_graph.add_edge('Pandora', 'Metroville', 82)

    cities_graph.add_edge('Arendelle', 'Metroville', 99)
    cities_graph.add_edge('Arendelle', 'Monstropolis', 42)

    cities_graph.add_edge('Metroville', 'Monstropolis', 105)
    cities_graph.add_edge('Metroville', 'Narnia', 37)
    cities_graph.add_edge('Metroville', 'Naboo', 26)
    
    cities_graph.add_edge('Naboo', 'Narnia', 250)
    cities_graph.add_edge('Naboo', 'Monstropolis', 73)
    print( get_direct_trips(cities_graph, ['Arendelle', 'Monstropolis', 'Naboo']))
    # print(cities_graph.get_neighbors('Monstropolis'))
    print( get_direct_trips(cities_graph, ['Monstropolis', 'Naboo', 'Narnia']))