# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = (l-1)
  pivot = arr[h]
  for j in range(l, h):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[h] = arr[h], arr[i+1]
  return (i+1) 
def quickSortIterative(arr, l, h):
  #write your code here
  if l < h:
    partition_index = partition(arr, l, h)
    quickSortIterative(arr, l, partition_index-1)
    quickSortIterative(arr, partition_index+1, h)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),

