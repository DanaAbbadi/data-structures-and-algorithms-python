from data_structures_and_algorithms.stacks_and_queues_challenges.node import Node
# from node import Node


class Stack(Node):
    
    def __init__(self):
        self.top = None

    def push(self, *args):
        """
            Takes a single or multiple values as an argument and adds the new nodes with that value to the front of the stack. 

            Arguments:
                *args -- list of values with variable length
        """
        for i in args:
            new_node = Node(i)
            temp = self.top
            self.top = new_node
            new_node.next = temp

    

    def pop(self):
        """
        * Removes the node from the front of the queue, and returns the node’s value. 
        * Will raise an exception if the queue is empty.
        """
        try:
            value = self.top.value
            self.top = self.top.next
            return value
        except AttributeError as error:
            return 'Stack is empty'
    
    def peek(self):
        """
        * Returns the value of the node located in the front of the queue, without removing it from the queue.
        * Will raise an exception if the queue is empty
        """
        try:
            return self.top.value
        except AttributeError as error:
            return 'Stack is empty'

    def isEmpty(self):
        """
        Checks whether or not the Queue is empty.
        """
        return False if self.top else True

    def __str__(self):
        current = self.top
        output = 'top->'
        while current:
            output += f"{current.value}->"
            current = current.next
        output+=" NULL"
        return output 




if __name__ == "__main__":
    adjectives = Stack()
    
    adjectives.push('smart','unique')
    adjectives.push('fluffy')

    print(adjectives)
    print(adjectives.pop())
    print(adjectives.peek())
    print(adjectives.isEmpty())



