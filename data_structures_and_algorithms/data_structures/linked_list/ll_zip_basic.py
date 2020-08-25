from linked_list_basic import (LinkedList,Node,)
# import data_structures_and_algorithms.data_structures.linked_list.linked_list_basic

def zipLists(a_list,b_list):
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


if __name__ == '__main__':

    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('berries')
    fruits.append('banana')
 
    veggies = LinkedList()
    veggies.append('Carrots')
    veggies.append('Broccoli')
    veggies.append('Mushrooms')
    
    print(zipLists(fruits,veggies))