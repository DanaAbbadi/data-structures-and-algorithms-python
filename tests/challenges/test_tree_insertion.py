import sys
sys.path.insert(1, '/home/dana/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import *
from data_structures_and_algorithms.tree.tree_basic import *

import pytest


def test_all_nodes_equal(prepare_same_trees):
    bt1 = prepare_same_trees[0]
    bt2 = prepare_same_trees[1]
    assert tree_intersection(bt1,bt2) == [15, 10, 8, 13, 25, 18, 50]

def test_different_locations(prepare_different_nodes_locations):
    bt1 = prepare_different_nodes_locations[0]
    bt2 = prepare_different_nodes_locations[1]
    assert tree_intersection(bt1,bt2) == [15]

def test_no_insertion(prepare_no_insertion):
    bt1 = prepare_no_insertion[0]
    bt2 = prepare_no_insertion[1]
    assert tree_intersection(bt1,bt2) == None

def test_empty_tree(prepare_empty_tree):
    bt1 = prepare_empty_tree[0]
    bt2 = prepare_empty_tree[1]
    assert tree_intersection(bt1,bt2) == None


def test_different_size(prepare_different_size):
    bt1 = prepare_different_size[0]
    bt2 = prepare_different_size[1]
    assert tree_intersection(bt1,bt2) == [15,10]




@pytest.fixture
def prepare_same_trees():
    bt1 = BinaryTree()
    bt1.root = Node(15)

    bt1.root.left = Node(10)
    bt1.root.left.left = Node(8)
    bt1.root.left.right = Node(13)

    bt1.root.right = Node(25)
    bt1.root.right.left = Node(18)
    bt1.root.right.right = Node(50)

    bt2 = BinaryTree()
    bt2.root = Node(15)

    bt2.root.left = Node(10)
    bt2.root.left.left = Node(8)
    bt2.root.left.right = Node(13)

    bt2.root.right = Node(25)
    bt2.root.right.left = Node(18)
    bt2.root.right.right = Node(50)

    return[bt1,bt2]

@pytest.fixture
def prepare_different_nodes_locations():
    bt1 = BinaryTree()
    bt1.root = Node(15)

    bt1.root.left = Node(20)
    bt1.root.right = Node(10)


    bt2 = BinaryTree()
    bt2.root = Node(15)

    bt2.root.left = Node(10)
    bt2.root.right = Node(20)

    return[bt1,bt2]

@pytest.fixture
def prepare_no_insertion():
    bt1 = BinaryTree()
    bt1.root = Node(7)

    bt1.root.left = Node(20)
    bt1.root.right = Node(10)


    bt2 = BinaryTree()
    bt2.root = Node(15)

    bt2.root.left = Node(10)
    bt2.root.right = Node(20)

    return[bt1,bt2]

@pytest.fixture
def prepare_empty_tree():
    bt1 = BinaryTree()
    
    bt2 = BinaryTree()
    bt2.root = Node(15)

    bt2.root.left = Node(10)
    bt2.root.right = Node(20)

    return[bt1,bt2]



@pytest.fixture
def prepare_different_size():
    bt1 = BinaryTree()
    bt1.root = Node(15)

    bt1.root.left = Node(10)
    bt1.root.left.left = Node(8)
    bt1.root.left.right = Node(13)

    bt1.root.right = Node(25)
    bt1.root.right.left = Node(18)
    bt1.root.right.right = Node(50)
    
    bt2 = BinaryTree()
    bt2.root = Node(15)

    bt2.root.left = Node(10)
    bt2.root.right = Node(20)

    return[bt1,bt2]










