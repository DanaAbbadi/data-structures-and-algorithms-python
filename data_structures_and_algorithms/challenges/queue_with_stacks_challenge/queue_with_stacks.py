# # from data_structures_and_algorithms.stacks_and_queues_challenges.stacks import Stack
# # from stacks import Stack

import sys
sys.path.insert(1, '/home/dana/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms.stacks_and_queues_challenges.stacks import Stack

# import sys
# sys.path.push("/home/dana/401/data-structures-and-algorithms-python")
# from data_structures_and_algorithms.stacks_and_queues_challenges.stacks import Stack

class PseudoQueue():

    def __init__(self):

        self.front_stack = Stack()
        self.rear_stack = Stack()
        self.len = 0

    def enqueue(self, value):
        """
        Push Node(value) to front_stack
        """
        self.len += 1
        self.front_stack.push(value)
    
    def dequeue(self):
        """
        Dequeue an item from the queue.
         1) If both stacks are empty, return stack is empty.
         2) If rear_stack is empty
            While front_stack is not empty, push everything from front_stack to rear_stack.
         3) Pop the element from rear_stack and return it.
        """
        if self.rear_stack.isEmpty():
            while self.len > 0:
                self.rear_stack.push(self.front_stack.pop())
                self.len-=1
            output = self.rear_stack.pop()

            while True:
                self.front_stack.push(self.rear_stack.pop())
                self.len +=1
                if self.rear_stack.isEmpty():
                    return output
        else:
            return "stack is empty!"



    def __str__(self):
        output = 'Rear ->'
        if self.front_stack.isEmpty():
            current = self.rear_stack.top
        else:
            current = self.front_stack.top
        while current:
            output += f"{{{current.value}}} -> "
            current = current.next
        output+=" Front"
        return output





if __name__ == "__main__":
    queue = PseudoQueue()
    
    queue.enqueue(4)

    queue.enqueue(5)
    # queue.enqueue(6)
    # queue.enqueue(7)
    # queue.enqueue(8)
    # queue.enqueue(9)

    # print(queue.dequeue())

    print(queue)
