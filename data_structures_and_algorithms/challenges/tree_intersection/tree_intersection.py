# from data_structures_and_algorithms.tree.tree_basic import *
import sys
sys.path.insert(1, '/home/dana/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms.tree.tree_basic import *

def tree_intersection(bt1,bt2):
    """
     Takes two Binary trees and returns their insertion; 
     the insertion occurs when two nodes have the same value and location in both trees.
    """
    output = []
    if not bt1.root or not bt2.root:
        return 
    def _walk(root1, root2):

        if root1 and root2:
            if root1.value == root2.value:
                output.append(root1.value)
            
            _walk(root1.left, root2.left)
            _walk(root1.right, root2.right)

    _walk(bt1.root, bt2.root)
    if output:
        return output
    return None