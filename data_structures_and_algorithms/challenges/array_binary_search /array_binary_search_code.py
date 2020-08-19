
def binarySearch(sortedArray, low, high, searchKey): 
  
    if high >= low: 
        mid = (high + low) // 2
        if sortedArray[mid] == searchKey: 
            return mid 

        elif sortedArray[mid] > searchKey: 
            return binarySearch(sortedArray, low, mid - 1, searchKey) 
  
        else: 
            return binarySearch(sortedArray, mid + 1, high, searchKey) 
  
    else: 
        return -1



# Test array 
# arr = [ 2, 3, 4, 10, 40 ] 
# x = 4
  
# # Function call 
# result = binarySearch(arr, 0, len(arr)-1, x) 
  
# if result != -1: 
#     print("Element is present at index", str(result)) 
# else: 
#     print("Element is not present in array")         