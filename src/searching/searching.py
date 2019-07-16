# STRETCH: implement Linear Search				
def linear_search(arr, target):
      for i in range( 0, len(arr) ):
          if arr[i] == target:
              return i
      return -1   


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  l = 0
  h = len(arr)-1

  while l < h:
        m = (l+h)/2
  if target < arr[m]:
        h = m-1 
  elif target > arr[m]:
        l = m+1 
  else:
        return m

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
