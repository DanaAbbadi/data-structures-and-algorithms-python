class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
    def __str__(self): 
        return self.value

class LinkedList(Node) :

    len_of_list=0

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
            LinkedList.len_of_list += 1

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
            LinkedList.len_of_list += 1

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
   
   
   
    def includes(self,value):
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
            LinkedList.len_of_list += 1

            current = self.head
            if not self.head:
                self.head = new_node
            else:
                # To add before the first node
                if self.head.value == value:
                    swap = self.head
                    self.head = new_node
                    new_node.next = swap
                    return 
                else:
                    current = self.head

                # To add anywhere in the list
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
            LinkedList.len_of_list += 1
             
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

    def kthFromEnd(self,k):
        try:
            if self.head:
                print(LinkedList.len_of_list)
                if k <= LinkedList.len_of_list and k>-1:
                        print('it is')
                        current = self.head
                        postion = LinkedList.len_of_list  - k
                        print('pos',postion)

                        for i in range(postion-1):
                            print('current',current)
                            current = current.next
                        return current.value


                
                else:
                        return 'The index you entered is invalid'

            else:
                return 'Linked List is empty'
        except Exception as error:
            print(f'this is error in this method {error}')

    def middle(self):
        if (LinkedList.len_of_list):
            middle = LinkedList.len_of_list //2
            current = self.head
            for i in range(middle):
                current=current.next 
            return current.value
        else:
            return 'List is empty'




if __name__ == "__main__":
    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('orange')
    fruits.append('banana')
    fruits.append('berries')
    fruits.append('grapes')


    # fruits.insert_before('apple','banana')
    # print( fruits.includes('banana'))
    # print(fruits)
    print(fruits.kthFromEnd(-1))
    print(fruits.middle())

    
