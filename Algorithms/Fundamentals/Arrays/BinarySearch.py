""" Binary Search: Binary search is an efficient algorithm for finding an element 
in a sorted array. It repeatedly divides the search interval in half. Time Complexity: 
O(log n)"""

def binary_search(arr, target):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1

arr = [10, 20, 30, 40, 50]
print(binary_search(arr, 30))  # Output: 2