from data_structures_and_algorithms.stacks_and_queues_challenges.queue import (Queue, Node)


def test_create_empty_Queue():
    nums = Queue()
    assert nums.front == None 

def test_enqueue_one_value():
    nums = Queue()
    nums.enqueue(1)
    assert nums.front.value == 1

def test_enqueue_multiple_values():
    nums = Queue()
    nums.enqueue(1,3,5,9)
    assert nums.front.value == 1
    assert nums.__str__() == 'front->1->3->5->9-> rear'

def test_dequeue():

    # Stand Alone testing:
    nums = Queue()
    node = Node(1)
    nums.rear = node
    nums.front = node  
    
    actual = nums.dequeue()
    expected = 1
    assert actual == expected

    # Using methods from Queue class:
    nums.enqueue(100,13)
    actual = nums.dequeue()
    expected = 100
    assert actual == expected

def test_dequeue_from_empty_Queue():
    nums = Queue()
    actual = nums.dequeue()
    expected = 'Queue is empty'
    assert actual == expected

def test_emptying_queue_with_multi_dequeue():
    nums = Queue()

    # Stand Alone testing:
    node = Node(1)
    nums.rear = node
    nums.front = node

    temp = nums.rear
    nums.rear = Node(13)
    temp.next = nums.rear

    nums.dequeue()
    nums.dequeue()

    actual = nums.dequeue()
    expected = 'Queue is empty'
    assert actual == expected

    # Using methods from Queue class:
    nums.enqueue(100,13)
    nums.dequeue()
    nums.dequeue()
    actual = nums.dequeue()
    expected = 'Queue is empty'
    assert actual == expected

def test_peek():
    nums = Queue()
    node = Node(13)
    nums.rear = node
    nums.front = node


    actual = nums.peek()
    expected = 13

    assert actual == expected

def test_peek_on_empty_Queue():
    nums = Queue()
    actual = nums.peek()
    expected = 'Queue is empty'
    assert actual == expected



    