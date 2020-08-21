def insert_shift_array(arr,val):

  if isinstance(val,int):

    if len(arr):
        for i in range(len(arr)):
          if arr[i]>val:
            break
        arr=arr[:i]+[val]+arr[i:]
        return arr
    else :
      arr.append(val)
      return arr
  
  else:
    return arr
    


