# from data_structures_and_algorithms.stacks_and_queues_challenges.node import Node
from node import Node


class Queue(Node):

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,*args):
        """
        Takes a single or multiple values as an argument and adds the new nodes with that value to the back of the queue. 

        Arguments:
            *args -- list of values with variable length
        """
        values=[]
        if not self.front and not self.rear:
            node = Node(args[0])
            self.front = node
            self.rear = node
            values = args[1:]
        else:
            values = args
        for i in values:
            temp = self.rear
            self.rear = Node(i)
            temp.next = self.rear

       
        

    def dequeue(self):
        """
        * Removes the node from the front of the queue, and returns the node’s value. 
        * Will raise an exception if the queue is empty.
        """
        try:
            value = self.front.value
            if self.front == self.rear:
                self.rear = None
            self.front = self.front.next

            return value
        
        except AttributeError:
            return 'Queue is empty'
    
    def peek(self):
        """
        * Returns the value of the node located in the front of the queue, without removing it from the queue.
        * Will raise an exception if the queue is empty.
        """
        try:
            return self.front.value
        except AttributeError:
            return 'Queue is empty'
    
    def isEmpty(self):
        """
        Checks whether or not the Queue is empty.
        """
        return False if self.front else True
        

    def __str__(self):
        current = self.front
        output = 'front->'
        while current:
            output += f"{current.value}->" 
            current = current.next
        output+=" rear"
        return output 



if __name__ == "__main__":
    nums = Queue()
    nums.enqueue(1)
    nums.enqueue(2,4)
    nums.enqueue(55,5)

    print(nums.dequeue())
    print(nums)
    print(nums.dequeue())
    print(nums.peek())
    print(nums.isEmpty())

  