
def partition(arr,low,high): 
    """
     This function takes last element as the pivot, places 
     the pivot element at its correct position where elements on the left
     are smaller, and all elemnts on the right are larger.
    """
    i = ( low-1 )          
    pivot = arr[high]      
  
    for j in range(low , high): 
        if   arr[j] < pivot:           
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  

  
def quickSort(arr,low,high): 
    """
     The main function that implements QuickSort 
     Arguments:
        arr[] --> Array to be sorted, 
        low  --> Starting index, 
        high  --> Ending index 
    """
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  

if __name__ == "__main__":
    
    arr = [10, 7, 8, 9, 1, 5] 
    n = len(arr) 
    quickSort(arr,0,n-1) 
    print (arr)