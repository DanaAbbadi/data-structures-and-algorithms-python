class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
     This class is responsible of creating and traversing the Binary Search Tree.

    """

    def __init__(self):
        self.root = None

    
    def breadth_first(self, root):
        """
        Traverse the tree using Breadth First approach where the Node Values at each level 
        of the Tree are traversed before going to next level.
        """
        try:
            queue = []
            breadth = []
            if not root:
                return 'Tree is empty'
            else:    
                if root:
                    queue.append(root)
                while queue:
                    current = queue.pop(0)
                    breadth.append(current.value)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
            return breadth
        except Exception as e:
            return f'An error occured, {e}'

if __name__ == "__main__":
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

    # 2 7 5 2 6 9 5 11 4

    print(bt.breadth_first(bt.root))
