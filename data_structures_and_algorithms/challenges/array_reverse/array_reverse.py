

def reverseArray(list):
 reversedList = list[::-1]
 return reversedList


# def reverse_array(arr):
#     arr.reverse()
#     return arr

a = [int(s) for s in input().split()]
print(reverseArray(a)) 