from data_structures_and_algorithms.stacks_and_queues_challenges.stacks import (Stack, Node)

def test_create_empty_stack():
    nums = Stack()
    assert nums.top == None 

def test_push_one_value():
    nums = Stack()
    nums.push(1)
    assert nums.top.value == 1

def test_push_multiple_values():
    nums = Stack()
    nums.push(1,3,5,9)
    assert nums.top.value == 9
    assert nums.__str__() == 'top->9->5->3->1-> NULL'

def test_pop():
    nums = Stack()

    # Stand Alone testing:
    nums.top = Node(1)
    actual = nums.pop()
    expected = 1
    assert actual == expected

    # Using methods from Stack class:
    nums.push(100,13)
    actual = nums.pop()
    expected = 13
    assert actual == expected

def test_pop_from_empty_stack():
    nums = Stack()
    actual = nums.pop()
    expected = 'Stack is empty'
    assert actual == expected

def test_emptying_stack_with_multi_pop():
    nums = Stack()

    # Stand Alone testing:
    nums.top = Node(1)
    temp = nums.top
    nums.top = Node(13)
    nums.top.next = temp

    nums.pop()
    nums.pop()

    actual = nums.pop()
    expected = 'Stack is empty'
    assert actual == expected

    # Using methods from Stack class:
    nums.push(100,13)
    nums.pop()
    nums.pop()
    actual = nums.pop()
    expected = 'Stack is empty'
    assert actual == expected

def test_peek():
    nums = Stack()
    nums.top = Node(13)

    actual = nums.peek()
    expected = 13

    assert actual == expected

def test_peek_on_empty_stack():
    nums = Stack()
    actual = nums.peek()
    expected = 'Stack is empty'
    assert actual == expected



    