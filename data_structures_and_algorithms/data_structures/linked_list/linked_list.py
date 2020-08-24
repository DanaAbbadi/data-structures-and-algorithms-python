class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
    def __str__(self): 
        return self.value

class LinkedList :

    def __init__(self):
        self.head = None
   
    def insert(self,value):
        """
        Takes any value as an argument and adds a new node with that value to the head of the list.
        
        Arguments:
            a value to be added to the list
        """
        try:
            new_node = Node(value)
            if not self.head:
                self.head=new_node
            else:
                new_node.next = self.head
                self.head = new_node    
        except Exception as error:
            print(f'this is error in this method {error}')
    def append(self,value):
        """
        Takes any value as an argument and adds a new node with that value to the end of the list.
        
        Arguments:
            a value to be added to the list
        """
        try:
            new_node = Node(value)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
        except Exception as error:
            print(f'this is error in this method {error}')
  
    def __str__(self):  
        current = self.head
        output = ''
        while current:
            output += f"{current.value}->"
            current = current.next
        output+=" NULL"
        return output 
   
   
   
    def includes (self,value):
        """
        method which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node's value somewhere within the list.
        
        Arguments:
            a value to search for
        """
        try:
            if self.head == None:
                return False
            else:
                current = self.head
                while current:
                    if current.value == value:
                        return True
                    else :
                        current = current.next    
                return False 
        except Exception as error:
            print(f'this is error in this method {error}')
    

    def insert_before(self,value,newValue):
        '''
        Add a new node with the given newValue immediately before the first value node 

        Arguments:
            value   --  Existing node
            new_val --  new node to add
        '''
        try:
            new_node = Node(newValue)
            current = self.head
            if not self.head:
                self.head = new_node
            else:
                
                while current.next != None:
                    if current.next.value == value:
                        swap = current.next
                        current.next = new_node
                        new_node.next = swap
                        return 
                    else:
                        current = current.next

                return "this node doesn't exist!"
        except Exception as error:
            print(f'this is error in this method {error}')        

    def insert_after(self, value, newVal):
        '''
        Add a new node with the given newValue immediately after the first value node 

        Arguments:
            value   --  Existing node
            new_val --  new node to add
        '''
        try:
            new_node = Node(newVal)
            current = self.head
            if not self.head:
                    self.head = new_node
            else:
                current = self.head
                while current.next != None:
                    if current.next.value == value:
                        current = current.next
                        temp = current.next
                        current.next = new_node
                        new_node.next = temp
                        return 
                        
                    else:
                        current = current.next
                        
                return "this node doesn't exist!"
        except Exception as error:
            print(f'this is error in this method {error}')
                        
                
if __name__ == "__main__":
    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('orange')
    fruits.append('berries')

    fruits.insert_after('berries','banana')

    # print( fruits.includes('banana'))
    print(fruits)
