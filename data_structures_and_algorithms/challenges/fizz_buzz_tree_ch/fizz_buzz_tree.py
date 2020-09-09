class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
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


def fizz_buzz(value):
    """
     Function to do fizz_buzz on the given value
     
    """
    if value % 15 == 0:
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    else:
        return str(value)

def fizz_buzz_tree(tree):
    """
     Function to change all values in the given tree according to fizz_buzz 
    """

    new_tree = BinaryTree()

    if not tree.root:
        return new_tree

    def replace_node(current):
        node = Node(fizz_buzz(current.value))

        if current.left:
            node.left = replace_node(current.left)
        if current.right:
            node.right = replace_node(current.right)
        return node


    new_tree.root = replace_node(tree.root)
    return new_tree

if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(10)
    tree.root.right = Node(9)

    new_tree = fizz_buzz_tree(tree)
    print(new_tree.root.value)
    print(new_tree.root.left.value)
    print(new_tree.root.right.value)
    print(new_tree.preOrder())

