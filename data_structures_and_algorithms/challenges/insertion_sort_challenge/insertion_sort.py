def insertion_sort(arr):

    """
     This function takes an array and sort it using insertion sort mechanism, then return it 
    """
    try:
        for i in range(1,len(arr)):
                        
            key = arr[i] 

            j = i - 1    

            while j >= 0 and key < arr[j] :   
                    arr[j + 1] = arr[j]      
                    j -= 1                  
            arr[j + 1] = key                

        return arr
    except Exception as error:
        print(f'This {error} occures during running')

