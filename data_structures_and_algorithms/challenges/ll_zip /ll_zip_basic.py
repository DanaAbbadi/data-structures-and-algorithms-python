# from linked_list_basic import (LinkedList,Node,)
# data_structures_and_algorithms/data_structures/linked_list/linked_list_basic.py
import sys
sys.path.insert(1, 'data_structures_and_algorithms/data_structures/linked_list')
from linked_list_basic import (LinkedList,Node,)

def zipLists(a_list,b_list):
    try:
        zipped = LinkedList()
        a_current,b_current = a_list.head,b_list.head
        zipped_len = a_list.len_of_list if a_list.len_of_list >= b_list.len_of_list else b_list.len_of_list

        for i in range(zipped_len):
            if a_current:
                zipped.append(a_current.value)
                a_current = a_current.next
            if b_current:
                zipped.append(b_current.value)
                b_current = b_current.next
        
        return zipped
    except Exception as error:
        print(f'You have an error in the method: {error}')

def to_sorted(a_list,b_list):

    sorted_list = LinkedList()

    first = a_list.head if a_list.head.value <= b_list.head.value else b_list.head
    second = b_list.head if a_list.head.value <= b_list.head.value else a_list.head
    
    while first:
        sorted_list.append(first.value)
        first = first.next
    while second:
        sorted_list.append(second.value)
        second = second.next
    return sorted_list



if __name__ == '__main__':

    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('berries')
    fruits.append('banana')
 
    veggies = LinkedList()
    veggies.append('Carrots')
    veggies.append('Broccoli')
    veggies.append('Mushrooms')
    
    # print(zipLists(fruits,veggies))

    num1 = LinkedList()
    num1.append(7)
    num1.append(8)
    num1.append(9)

    num2 = LinkedList()
    num2.append(4)
    num2.append(5)
    num2.append(6)

    # print('is sorted? ',to_sorted(num1,num2))