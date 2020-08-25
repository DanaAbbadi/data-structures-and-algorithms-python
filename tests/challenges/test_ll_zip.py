# from data_structures_and_algorithms.data_structures.linked_list.linked_list_basic import (LinkedList,Node,)
import sys
sys.path.insert(1, 'data_structures_and_algorithms/challenges/ll_zip ')
from ll_zip_basic import (zipLists,LinkedList,Node,to_sorted,)

# from data_structures_and_algorithms.challenges.ll_zip.ll_zip_basic import (zipLists,)
# data_structures_and_algorithms/challenges/ll_zip /ll_zip_basic.py
# data_structures_and_algorithms/challenges/ll_zip /ll_zip_basic.py

def test_zip():
    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('berries')
    fruits.append('banana')
 
    veggies = LinkedList()
    veggies.append('Carrots')
    veggies.append('Broccoli')
    veggies.append('Mushrooms')

    lst = zipLists(fruits,veggies)
    assert lst.__str__() == 'apple->Carrots->berries->Broccoli->banana->Mushrooms-> NULL'


def test_zip1():
    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('berries')
 
    veggies = LinkedList()
    veggies.append('Carrots')
    veggies.append('Broccoli')
    veggies.append('Mushrooms')

    lst = zipLists(fruits,veggies)
    assert lst.__str__() == 'apple->Carrots->berries->Broccoli->Mushrooms-> NULL'


def test_zip_nums():
    num1 = LinkedList()
    num1.append('5')
    num1.append('2')
 
    num2 = LinkedList()
    num2.append('7')
    num2.append('9')
    num2.append('10')
    num2.append('4')
    num2.append('5')

    lst = zipLists(num1,num2)
    assert lst.__str__() == '5->7->2->9->10->4->5-> NULL'

def test_zip_nums1():
    num1 = LinkedList()
    num1.append('5')
    num1.append('2')
 
    num2 = LinkedList()
    num2.append('7')
    
    lst = zipLists(num1,num2)
    assert lst.__str__() == '5->7->2-> NULL'

def test_zip_nums2():
    num1 = LinkedList()
    num1.append('5')
    num1.append('2')
 
    num2 = LinkedList()
    num2.append('7')
    
    lst = zipLists(num1,num2)

    assert lst.__str__() == '5->7->2-> NULL'

def test_zip_null():
    num1 = LinkedList() 
    num2 = LinkedList()    
    lst = zipLists(num1,num2)
    assert lst.__str__() == ' NULL'

def test_sorted():
    num1 = LinkedList()
    num1.append('5')
    num1.append('6')

    num2 = LinkedList()
    num2.append('3')
    num2.append('4')

    lst = to_sorted(num1,num2)
    assert lst.__str__() == '3->4->5->6-> NULL'