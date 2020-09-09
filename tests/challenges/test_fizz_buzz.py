from data_structures_and_algorithms.challenges.fizz_buzz_tree_ch.fizz_buzz_tree import *
import pytest


def test_fizz_buzz(prepare_binary_tree):
    bt = prepare_binary_tree
    fizz_buzz = fizz_buzz_tree(bt)
    assert fizz_buzz.preOrder() == ['2', 'FizzBuzz', 'Fizz', 'Fizz', '4', '11', 'Buzz', 'Fizz', 'Buzz']

def test_no_fizz_buzz(prepare_binary_tree2):
    bt = prepare_binary_tree2
    fizz_buzz = fizz_buzz_tree(bt)
    assert fizz_buzz.preOrder() == ['2', '7', '2', '8', '16', '11', '4']














@pytest.fixture
def prepare_binary_tree():
    bt = BinaryTree()
    bt.root = Node(2)

    bt.root.left = Node(15)  
    bt.root.right = Node(5)  

    bt.root.left.left = Node(9)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(4)  
    bt.root.left.right.right = Node(11)  


    bt.root.right.right = Node(21)
    bt.root.right.right.left = Node(20) 

    return bt

@pytest.fixture
def prepare_binary_tree2():
    bt = BinaryTree()
    bt.root = Node(2)

    bt.root.left = Node(7)  
    bt.root.right = Node(4)  

    bt.root.left.left = Node(2)
    bt.root.left.right = Node(8)
    bt.root.left.right.left = Node(16)  
    bt.root.left.right.right = Node(11)  



    return bt








