
""" Linear Search: Linear search is a simple technique where you 
iterate over the entire array to find an element. Time Complexity: O(n)."""

def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1

arr = [10, 20, 30, 40]
print(linear_search(arr, 30))