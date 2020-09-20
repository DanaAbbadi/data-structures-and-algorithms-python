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


## visualization

Let's take the following array: [25, 17, 31, 13, 2], we will walk through iterations, starting with the first one:

##### First Iteration: 

Compare 25 with 17. The comparison shows 17< 25. Hence swap 17 and 25.
The array now looks like:
[17, 25, 31, 13, 2]

![first iteration](https://s3-us-west-2.amazonaws.com/tutorials-image/first+iteration.png)

##### Second Iteration: 

Now hold on to the next element (31) and compare with the ones before it.
Since 31> 25, no swapping takes place.
Also, 31> 17, no swapping takes place and 31 remains at its position.
The array after the Second iteration looks like:

[17, 25, 31, 13, 2]

![2nd iteration](https://s3-us-west-2.amazonaws.com/tutorials-image/second+iteration.png)

##### Third Iteration: 

Start the following Iteration with the fourth element (13), and compare it with its preceding elements.

Since 13< 31, we swap the two.

Array now becomes: [17, 25, 13, 31, 2].

We will keep comparing all preceding elements with 13. Now the comparison is between 25 and 13. Since, 13 < 25, we swap the two.

The array becomes [17, 13, 25, 31, 2].

The last comparison for the iteration is now between 17 and 13. Since 13 < 17, we swap the two.

The array now becomes [13, 17, 25, 31, 2].

![img](https://s3-us-west-2.amazonaws.com/tutorials-image/working+of+insertion+sort.png)

##### Fourth Iteration: 

The last iteration is for the last element (2), with all the preceding elements and make the appropriate swapping between elements.

Since, 2< 31. Swap 2 and 31.

Array now becomes: [13, 17, 25, 2, 31].

Compare 2 with 25, 17, 13.

Array now becomes: [13, 2, 17, 25, 31].

The last comparison for the Iteration is to compare 2 with 13.

Since 2< 13. Swap 2 and 13.

The array now becomes:

**[2, 13, 17, 25, 31]**.

This is the final array after all the corresponding iterations and swapping of elements.

![last](https://s3-us-west-2.amazonaws.com/tutorials-image/insertion-sort.png)










