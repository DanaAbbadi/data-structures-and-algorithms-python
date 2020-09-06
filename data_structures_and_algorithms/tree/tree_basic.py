class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
     This class is responsible of traversing the Binary Search Tree by following Depth First approach.

    """

    def __init__(self):
        self.root = None

    def preOrder(self):
        """
         * Traverse the Bianay tree by pre-order approach as: root >> left >> right.
         * Returns a list of all the nodes in the tree.

        """
        try:
            output = []
            
            def loop_through(node):
                if not node:
                    return

                output.append(node.value)
                loop_through(node.left)
                loop_through(node.right)
            
            loop_through(self.root)
            return output
        except Exception as error:
            return f'An error occured during excuting: {error}'
    
    def in_order(self,root):
        """
         * Traverse the Bianay tree by in-order approach as: left >> root >> right.
         * Returns a list of all the nodes in the tree.

        """
        try:
            output = []
            if root:
                output = self.in_order(root.left)
                output.append(root.value)
                output = output + self.in_order(root.right)
            return output
        except Exception as error:
            return f'An error occured during excuting: {error}'


    def post_order(self,root):
        """
         * Traverse the Bianay tree by post-order approach as: left >> right >> root.
         * Returns a list of all the nodes in the tree.

        """
        try:

            output = []
            if root:
                output = self.post_order(root.left)
                output = output + self.post_order(root.right)
                output.append(root.value)
            return output

        except Exception as error:
            return f'An error occured during excuting: {error}'

    def find_maximum_value(self,current):
        """
        Finds the maximum value in the binary tree.
        Will be called recursively with current equall to root.left and root.right
        
        """

        if not self.root:
            return 'Tree is empty'
        
        else:
            max = current.value

            if current.left != None:
                left_max = self.find_maximum_value(current.left)
                if left_max > max:
                    max = left_max

            if current.right != None:
                right_max = self.find_maximum_value(current.right)
                if right_max > max:
                    max = right_max
        
        return max





class BinarySearchTree(BinaryTree):
    """
     * This class is responible for adding new nodes to te tree following binary search approach
       keeping the tree always sorted, and the root is always the middle value.

     * Search the tree for a spesific value

    """

    def add(self,value):
        """
         Adds a new node in the correct location in the binary search tree.

         Arguments:
            value -- value of the new node

        """

        node = Node(value)
        if not self.root:
            self.root = node

        else:
            current = self.root
            while current:

                if node.value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = node
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node 
                        break
    
    def contains(self,node,value):
        """
         Returns a boolean indicating whether or not the value is in the tree at least once.

         Arguments:
            node  -- to map through the tree either to the left or right of the root, depends on the value.
            value -- value of the node to be searched.

         Output:
            Boolean -- Whether the node exists in the tree or not.

            
        """
        try:
            if node:
                if node.value == value:
                    return True
                elif node.value > value  :
                    return self.contains(node.left,value)
                elif value > node.value:
                    return self.contains(node.right,value)
            else:
                return False
        except Exception as error:
            return f'{error}'


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.add(23)

    # Add to the left
    tree.add(10)
    tree.add(9)
    tree.add(5)
    tree.add(15)

    # Add to the Right
    tree.add(35)
    tree.add(27)
    tree.add(96)

    # pre_order  = 23 10 9 5 15 35 27 96
    # in_order   = 5 9 10 15 23 27 35 96
    # post_order = 5 9 15 10 27 96 35 23

    pre_order = tree.preOrder()
    in_order = tree.in_order(tree.root)
    post_order = tree.post_order(tree.root)

 
    bt = BinaryTree()
    bt.root = Node(2)

    bt.root.left = Node(7)  
    bt.root.right = Node(5)  

    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)  
    bt.root.left.right.right = Node(11)  


    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)  


    print(bt.find_maximum_value(bt.root))
    print(tree.find_maximum_value(tree.root))



