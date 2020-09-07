from data_structures_and_algorithms.challenges.binary_tree.breadth_first import *
import pytest


def test_breadth_first(prepare_binary_tree):
    bt = prepare_binary_tree
    breadth_first = bt.breadth_first(bt.root)
    assert breadth_first == [2, 7, 5, 2, 6, 9, 5, 11, 4]

def test_empty_tree():
    bt = BinaryTree()
    assert bt.breadth_first(bt.root) == 'Tree is empty'






@pytest.fixture
def prepare_binary_tree():
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

    return bt

