def insertShiftArray(arr,val):
      for i in range(len(arr)):
        if arr[i]>val:
          break
      arr=arr[:i]+[val]+arr[i:]
      return arr
    
# print(insertShiftArray([1,2,4,5],3))


