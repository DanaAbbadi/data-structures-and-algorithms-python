from data_structures_and_algorithms.challenges.queue_with_stacks_challenge.queue_with_stacks import PseudoQueue

def test_enqueue():
    queue = PseudoQueue()
    queue.enqueue(4)
    queue.enqueue(5)
    assert queue.__str__() == 'Rear ->{5} -> {4} ->  Front'

def test_dequeue():
    queue = PseudoQueue()
    queue.enqueue(4)
    queue.enqueue(5)
    assert queue.dequeue() == 4