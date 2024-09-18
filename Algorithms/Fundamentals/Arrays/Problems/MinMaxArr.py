"""Problem 1: Finding the Maximum and Minimum in an Array
Write a function to find the maximum and minimum elements in an array."""

def find_max_min(arr):
  return max(arr), min(arr)

arr = [10, 20, 30, 50]
print(find_max_min(arr)) # Output: (50, 10)