from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,Node,
)


def test_empty_list():
    ll = LinkedList()
    assert ll.head == None

def test_head():
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    assert ll.head.value == 5

def test_insert_to_empty_ll():
    ll = LinkedList()
    ll.insert(5)
    assert ll.head.value == 5

def test_multiple_insert():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(7)
    assert ll.__str__() == '7->6->5-> NULL'

def test_includes():
    ll = LinkedList()
    ll.insert(5)
    assert ll.includes(5) == True

def test_includes_false():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(77)
    ll.insert(75)
    assert ll.includes(6) == False

def test_dender_str():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(7)
    assert ll.__str__() == '7->6->5-> NULL'
