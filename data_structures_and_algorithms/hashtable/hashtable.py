from data_structures_and_algorithms.hashtable.linked_list import Linkedlist
# from linked_list import Linkedlist


class HashTable:
    def __init__(self, size=1024):
        self.map = [None] * size
        self.size = size
        self.current = None
    
    def hash(self, key):
        """
         Takes a key and returns the index where it will
         be stored in the map list.
    
        """
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)
        return hash_sum*13 % 1024 

    def contains(self, key):
        """
         Takes in the key and returns a boolean,
         indicating if the key exists in the table already.

        """
        try:
            hashed = self.hash(key)
            if self.map[hashed]:
                self.current = self.map[hashed].head 
                while self.current:
                    if self.current.data[0] == key:
                        return True
                    self.current = self.current.next
            return False

        except Exception as error:
            print(f'{error}')

    def add(self, key, value):
        """
        Takes in both the key and value, it will hash the key, 
        and add the key and value pair to the map list, 
        handling collisions as needed.
        
        """
        try:
            hashed = self.hash(key)

            if self.map[hashed] == None:
                self.map[hashed] = Linkedlist()

            includes = self.contains(key)
            if includes:
                self.current.data[1] = value
            else:
                self.map[hashed].add([key, value])

        except Exception as error:
            print(f'{error}')
            


    def get(self, key):
        """
         Takes in the key and returns the value from the table.

        """
        try:

            hashed = self.hash(key)
            
            if self.map[hashed]:
                includes = self.contains(key)
                if includes:
                    return self.current.data[1] 
            
            return 'Not in the table'

        except Exception as error:
            print(f'{error}')