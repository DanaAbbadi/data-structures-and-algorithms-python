from data_structures_and_algorithms.data_structures.linked_list.linked_list_basic import (LinkedList,Node,)


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

def test_insert_before():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(8)
    ll.insert(9)
    ll.insert_before(6,7)
    assert ll.__str__() == '9->8->7->6->5-> NULL'


def test_insert_before_first_node():
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(8)
    ll.append(9)
    ll.insert_before(5,4)
    assert ll.__str__() == '4->5->6->8->9-> NULL'

def test_insert_after():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(8)
    ll.insert(9)
    ll.insert_after(8,7)
    assert ll.__str__() == '9->8->7->6->5-> NULL'

def test_insert_after_last_node():
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(8)
    ll.append(9)
    ll.insert_after(9,10)
    assert ll.__str__() == '5->6->8->9->10-> NULL'


def test_kthFromEnd():
    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('orange')
    fruits.append('berries')
    assert fruits.kthFromEnd(0) == 'berries'

def test_kthFromEnd_middle():
    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('orange')
    fruits.append('berries')
    assert fruits.kthFromEnd(1) == 'orange'

def test_kthFromEnd_k_greater():
    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('orange')
    fruits.append('berries')
    assert fruits.kthFromEnd(7) == 'The index you entered is invalid'

def test_kthFromEnd_k_equal():
    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('orange')
    fruits.append('berries')
    assert fruits.kthFromEnd(3) == 'The index you entered is invalid'

def test_kthFromEnd_k_negative():
    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('orange')
    fruits.append('berries')
    assert fruits.kthFromEnd(-1) == 'The index you entered is invalid'

def test_kthFromEnd_Length_1():
    fruits = LinkedList()
    fruits.append('apple')
    LinkedList.len_of_list = 1
    assert fruits.kthFromEnd(0) == 'apple'