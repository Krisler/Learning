"""Bubble Sort: Bubble sort repeatedly steps through the list, compares adjacent 
elements, and swaps them if they are in the wrong order. Time Complexity: O(n^2)."""

def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - 1 - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1] , arr[j]

arr = [64, 25, 12, 22, 11]
bubble_sort(arr)
print(arr)