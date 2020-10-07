import sys
sys.path.insert(1, '/home/dana/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms.challenges.get_edge.get_edge import *
import pytest

def test_trip_1(cities_graph):
    graph = cities_graph
    assert get_direct_trips(graph, ['Metroville', 'Pandora']) == 'True, $82'


def test_trip_2(cities_graph):
    graph = cities_graph
    assert get_direct_trips(graph, ['Arendelle', 'Monstropolis', 'Naboo']) == 'True, $115'

def test_no_direct_path1(cities_graph):
    graph = cities_graph
    assert get_direct_trips(graph, ['Naboo', 'Pandora']) == 'False, $0'

def test_no_direct_path2(cities_graph):
    graph = cities_graph
    assert get_direct_trips(graph, ['Narnia', 'Arendelle', 'Naboo']) == 'False, $0'


def test_city_not_in_graph(cities_graph):
    graph = cities_graph
    assert get_direct_trips(graph, ['Metroville', 'Pandora', 'Amman']) == 'False, $0'







@pytest.fixture
def cities_graph():
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

    return cities_graph
