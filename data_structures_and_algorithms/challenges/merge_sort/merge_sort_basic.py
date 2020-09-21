def merge_sort(myList):

    if len(myList) > 1:

        mid = len(myList) // 2
        
        # Divide into two lists
        left = myList[:mid]
        right = myList[mid:]

        # Recursive tell list length is 1, to return None
        merge_sort(left)
        merge_sort(right)

        # Two iterators for both lists, they will loop through all elements 
        i = 0
        j = 0

        # Iterator for the main list at each iteration
        k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
              myList[k] = left[i]
              i += 1

            else:
                myList[k] = right[j]
                j += 1

            # Move to the next slot
            k += 1


        # If there is remaining values left in one of the two lists:
        # For the left list
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        # For the right list
        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

if __name__ == "__main__":
    arr = [8,4,23,42,16,15]
    print(merge_sort(arr))