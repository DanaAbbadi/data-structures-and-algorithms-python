# Merge Sort

Merge sort is a *divide-and-conquer* algorithm based on the idea of breaking down a list into several sub-lists until each sublist consists of a single element and merging those sublists in a manner that results into a sorted list. Merge sort divides input array in two halves, left and right, calls itself for the two halves and then merges the two sorted halves. 

_______
## How merge sort works 

**Top-down Merge Sort Implementation:**
The top-down merge sort approach is the methodology which uses recursion mechanism. It starts at the Top and proceeds downwards, with each recursive turn it splits the array into two, make a recursive call again, and merge the results, until one gets to the bottom of the array-tree.


__________

## Algorithm

    MergeSort(arr[])
    If len(arr) > l
        1. Find the middle point to divide the array into two halves:  
                middle mid = (l+len(arr))/2
        2. Call mergeSort for left half:   
                Call mergeSort(arr[:mid])
        3. Call mergeSort for right half:
                Call mergeSort(arr[mid:])
        4. Merge the two halves sorted in step 2 and 3:
                
_______

## Pseudo Code

    ALGORITHM Mergesort(arr)
        DECLARE n <-- arr.length
            
        if n > 1
        DECLARE mid <-- n/2
        DECLARE left <-- arr[0...mid]
        DECLARE right <-- arr[mid...n]
        // sort the left side
        Mergesort(left)
        // sort the right side
        Mergesort(right)
        // merge the sorted left and right sides together
        Merge(left, right, arr)

    ALGORITHM Merge(left, right, arr)
        DECLARE i <-- 0
        DECLARE j <-- 0
        DECLARE k <-- 0

        while i < left.length && j < right.length
            if left[i] <= right[j]
                arr[k] <-- left[i]
                i <-- i + 1
            else
                arr[k] <-- right[j]
                j <-- j + 1
                
            k <-- k + 1

        if i = left.length
        set remaining entries in arr to remaining values in right
        else
        set remaining entries in arr to remaining values in left

## Trace

Let's trace the following list:  **[8,4,23,42,16,15]**




* Devide the list into two halves
  
<img src= '/assets/merge/1.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

* Call the merge function recursively for both lists, the left and right one.
   
   - Left_list  = [8,4,23]
   - Right_list = [42,16,15]

* We will trace the left one, since the same process will be applied to the right one.
* Again divide the left list into two lists, as follows:
  
     - Left_list  = [8,4]
     - Right_list = [23]
  
<img src= '/assets/merge/2.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

* Calling mergeSort again, for the left list it will be divided once again, however, for the right one, no more dividing it's ready to be compared, so it will wait for the left list to be sorted. The resulted lists from deviding the left list are:
  
     - Left_list  = [8]
     - Right_list = [4]
  
<img src= '/assets/merge/3.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

* Since the length of each list is 1, no more division. It's time to compare and sort them.

<img src= '/assets/merge/4.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

* Now back to right_list = [23], it will be compared to the sorted list [4,8]:

<img src= '/assets/merge/5.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

* The resulted list so far is [4,8,23], this is the first left list, the same process for the right list [42,16,15]

<img src= '/assets/merge/6.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

* Following the same process, this is the final result for the right list

<img src= '/assets/merge/7.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

* Now, the left and right lists will be compared together, element by element following the iterators i,j and k.

<img src= '/assets/merge/8.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>

* The final result:

<img src= '/assets/merge/10.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '> 

_______________________________

## Merge Sort Complexity

### Time Complexity

Best Case Complexity: O(n*log n)

Worst Case Complexity: O(n*log n)

Average Case Complexity: O(n*log n)

### Space Complexity

The space complexity of merge sort is O(n).

