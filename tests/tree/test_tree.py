from data_structures_and_algorithms.tree.tree_basic import (Node,BinarySearchTree,BinaryTree,)
import pytest

# Testing BinaryTree class
def test_empty_BinaryTree():
    bt = BinaryTree()
    assert bt.root == None

def test_pre_oreder(prepare_bt):
    bt = prepare_bt
    pre_order_list = bt.preOrder()
    assert pre_order_list == [15,10,8,13,25,18,50]

def test_in_oreder(prepare_bt):
    bt = prepare_bt
    pre_order_list = bt.in_order(bt.root)
    assert pre_order_list == [8, 10, 13, 15, 18, 25, 50]

def test_post_oreder(prepare_bt):
    bt = prepare_bt
    pre_order_list = bt.post_order(bt.root)
    assert pre_order_list == [8, 13, 10, 18, 50, 25, 15]



# Testing BinarySearchTree class

def test_add_root():
    bst = BinarySearchTree()
    bst.add(13)
    assert bst.root.value == 13

def test_add_multi_nodes(prepare_bst):
    bst = prepare_bst
    assert bst.root.value == 15

    assert bst.root.left.value == 10
    assert bst.root.left.left.value == 8
    assert bst.root.left.right.value == 13

    assert bst.root.right.value == 25
    assert bst.root.right.left.value == 18
    assert bst.root.right.right.value == 50

def test_contains(prepare_bst):
    bst = prepare_bst
    assert bst.contains(bst.root,15) == True
    assert bst.contains(bst.root,100) == False












@pytest.fixture
def prepare_bt():
    bt = BinaryTree()
    bt.root = Node(15)

    bt.root.left = Node(10)
    bt.root.left.left = Node(8)
    bt.root.left.right = Node(13)

    bt.root.right = Node(25)
    bt.root.right.left = Node(18)
    bt.root.right.right = Node(50)



    return bt



@pytest.fixture
def prepare_bst():
    bst = BinarySearchTree()
    bst.add(15)

    bst.add(10)
    bst.add(8)
    bst.add(13)

    bst.add(25)
    bst.add(18)
    bst.add(50)

    return bst




