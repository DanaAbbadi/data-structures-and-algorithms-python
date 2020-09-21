# Insertion Sort

Insertion sort is the sorting mechanism where the sorted array is built having one item at a time. The array elements are compared with each other sequentially and then arranged simultaneously in some particular order. The analogy can be understood from the style we arrange a deck of cards. This sort works on the principle of inserting an element at a particular position, hence the name Insertion Sort.

## How Insertion Sort works

1. The first element in the array is assumed to be sorted. Take the second element and store it separately in key.
2. Compare key with the first element. If the first element is greater than key, then key is placed in front of the first element.
3. Take the next element and compare it with the elements on the left of it. Placed it just behind the element smaller than it. If there is no element smaller than it, then place it at the beginning of the array.
4. Similarly, place every unsorted element at its correct position.

### Pseudocode

    SelectionSort(int[] arr)
        DECLARE n <-- arr.Length;
        FOR i = 0; i to n - 1  
            DECLARE min <-- i;
            FOR j = i + 1 to n
                if (arr[j] < arr[min])
                    min <-- j;

            DECLARE temp <-- arr[min];
            arr[min] <-- arr[i];
            arr[i] <-- temp;


## Trace 

Let's take the following array: [8,4,23,42,16,15], we will walk through iterations:

<img src= '/assets/sort/arr.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

##### First Iteration: 

Compare 4 with 8. 
  * Since 4 < 8, swap them.
  * The array now looks like:
     [4,8,23,42,16,15]

<img src= '/assets/sort/1.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

##### Second Iteration: 

The next element is (23).
  * Since 23 > 8, no swapping takes place.
  * Also, 23 > 4, no swapping takes place
  * 23 remains at its position.
  * The array after the Second iteration looks like:

      [4,8,23,42,16,15]

<img src= '/assets/sort/2.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

##### Third Iteration: 

The next element is (42).
  * Since 42 > 23, no swapping takes place.
  * Also, 42 > 8, no swapping takes place
  * 42 remains at its position.
  * The array after the Second iteration looks like:

      [4,8,23,42,16,15]

<img src= '/assets/sort/2.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

##### Forth Iteration: 

The fourth element is (16),  compare it with its preceding elements.

  * Since 16 < 42, we swap the two.

    -  Array now becomes: [4,8,23,16,42,15].

  * Now the comparison is between 16 and 23. Since, 16 < 23, we swap the two.

    - The array becomes [4,8,16,23,42,15].

  * The last comparison for the iteration is now between 16 and 8. Since 16 > 8, No swap needed.

  * The array now becomes [4,8,16,23,42,15]

<img src= '/assets/sort/3.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

##### Fifth Iteration: 

The last iteration is for the last element (15), with all the preceding elements and make the appropriate swapping between elements.

  * Since, 15 < 42. Swap them.

    - Array now becomes: [4,8,16,23,15,42].

  * Compare 15 with 23, 16.

    - Array now becomes: [4,8,15,16,23,42].


The array now becomes:

**[4,8,15,16,23,42]**.

This is the final array after all the corresponding iterations and swapping of elements.

<img src= '/assets/sort/4.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

## Final Code

``` python

def insertion_sort(arr):
    for i in range(1,len(arr)):
                     
        key = arr[i] 

        j = i - 1    

        while j >= 0 and key < arr[j] :   
                arr[j + 1] = arr[j]      
                j -= 1                  
        arr[j + 1] = key                

    return arr

```

## Complexity

### Time Complexity

Let's study the worst Case senario:

Suppose, an array is in ascending order, and you want to sort it in descending order.

Each element has to be compared with each of the other elements so, for every nth element, (n-1) number of comparisons are made.

Thus, the total number of comparisons = n*(n-1) ~ n2

### Space Complexity

Space complexity is O(1) because an extra variable key is used.





