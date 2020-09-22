# Quick Sort

QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways:

* Always pick first element as pivot.
* Always pick last element as pivot (implemented below)
* Pick a random element as pivot.
* Pick median as pivot.

The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x.

##### Technically, quick sort follows the below steps:

Step 1 − Make any element as pivot
Step 2 − Partition the array on the basis of pivot
Step 3 − Apply quick sort on left partition recursively
Step 4 − Apply quick sort on right partition recursively

_______________________

## Pseudo Code

    ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

        ALGORITHM Partition(arr, left, right)
            // set a pivot value as a point of reference
            DEFINE pivot <-- arr[right]
            // create a variable to track the largest index of numbers lower than the defined pivot
            DEFINE low <-- left - 1
            for i <- left to right do
                if arr[i] <= pivot
                    low++
                    Swap(arr, i, low)

            // place the value of the pivot location in the middle.
            // all numbers smaller than the pivot are on the left, larger on the right. 
            Swap(arr, right, low + 1)
            // return the pivot index point
            return low + 1

        ALGORITHM Swap(arr, i, low)
            DEFINE temp;
            temp <-- arr[i]
            arr[i] <-- arr[low]
            arr[low] <-- temp

_______________

## Trace

Let's trace the following list:  **[8,4,23,42,16,15]**

**Step 1**: Select the pivot.
  
<img src= '/assets/quick/1.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

**Step 2**: Move the pivot to the end.
  
<img src= '/assets/quick/2.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

**Step 3**: Partition the subarray.
  
<img src= '/assets/quick/3.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

**Step 4**: Move the left bound to the right until it reaches a value greater than or equal to the pivot.
  
<img src= '/assets/quick/4.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

**Step 5**: That is as far as we go this round.
  
<img src= '/assets/quick/5.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

**Step 6**: Move the right bound to the left until it crosses the left bound or finds a value less than the pivot. That is as far as we go this round.
  
<img src= '/assets/quick/6.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

**Step 7**: Swap the selected values.
  
<img src= '/assets/quick/7.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

**Step 8**: Move the left bound to the right until it reaches a value greater than or equal to the pivot.
  
<img src= '/assets/quick/8.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

**Step 9**: That is as far as we go this round.
  
<img src= '/assets/quick/9.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

**Step 10**: Move the right bound to the left until it crosses the left bound or finds a value less than the pivot.
  
<img src= '/assets/quick/10.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

**Step 11**: When the right bound crosses the left bound, all elements to the left of the left bound are less than the pivot and all elements to the right are greater than or equal to the pivot.
  
<img src= '/assets/quick/11.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

**Step 12**: Move the pivot to its final location.
  
<img src= '/assets/quick/12.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

**Step 13**: Call quicksort on the left sublist, select a new pivot and repeate the same process. This the final sorted list :

<img src= '/assets/quick/13.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>
_______________________________

## Quick Sort Complexity

### Time Complexity

Time complexity Big O(n^2)

### Space Complexity

Space complexity Big O(log(n))

