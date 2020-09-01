# from data_structures_and_algorithms.challenges.fifo_animal_shelter_challenge.fifo_animal_shelter import *
# import sys
# sys.path.insert(1, 'data_structures_and_algorithms/challenges/fifo_animal_shelter_challenge')

from data_structures_and_algorithms.challenges.fifo_animal_shelter_challenge.fifo_animal_shelter import (Animal,AnimalShelter)


def test_enqueue():
    animals=AnimalShelter()
    animals.enqueue('cherry','cat')
    expected='cherry'
    actual=animals.front.name
    assert actual==expected


def test_last_enqueue():
    animals=AnimalShelter()

    animals.enqueue('cherry','cat')
    animals.enqueue('oscar','dog')
    animals.enqueue('bo','dog')

    expected = 'front->cherry->oscar->bo-> rear'
    actual = animals.__str__()
    assert actual == expected

def test_dequeue_first_object():
    animals=AnimalShelter()

    animals.enqueue('cherry','cat')
    animals.enqueue('oscar','dog')
    animals.enqueue('bo','dog')
    animals.dequeue('cat')
    expected ='front->oscar->bo-> rear'
    actual = animals.__str__()
    assert actual == expected



def test_dequeue_second_object():
    animals=AnimalShelter()

    animals.enqueue('cherry','cat')
    animals.enqueue('oscar','dog')
    animals.enqueue('bo','dog')

    animals.dequeue('dog')
    expected = 'front->cherry->bo-> rear'
    actual = animals.__str__()
    assert actual == expected






def test_dequeue_None():
    animals=AnimalShelter()

    expected = 'No items in queue!'
    actual = animals.dequeue('cat')
    assert actual == expected
