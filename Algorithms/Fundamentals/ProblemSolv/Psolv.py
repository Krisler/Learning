#Step 1: Problem Definition
#Example

# Problem: Given an array of integers, find two numbers that add up to a target value.
#Input: arr = [2, 7, 11, 15], target = 9
#Output: Indices of the two numbers that add up to the target (e.g., [0, 1]).

#Step 2: Break Down the Problem
#Decompose the problem into smaller steps:

#Iterate over the array to pick a number.
#For each number, find another number that, when added, gives the target.
#Return the indices of both numbers.

#Step 2: Choosing a Data Structure
#The choice of data structure depends on the problem. For example:

#Arrays or lists for sequential data.
#Hash tables for quick lookups.
#Stacks or queues for order-based tasks.
#In the above example, we can use a hash table to store the elements for quick look-up.

#Step 4: Choosing an Algorithm
#You could use:

#Brute Force: Check all pairs of numbers.
#Hash Map: Store each number in a hash map and check if the complement  
#          (target - number) exists.
#Hash Map is more efficient because it reduces the complexity to O(n).

#Step 5: Pseudocode and Plan
#Before jumping to code, write a plan or pseudocode
#Pseudocode for the two-sum problem:

#Create an empty hash map
#For each element in the array:
#    Check if (target - element) exists in the hash map
#    If yes, return indices
#    If no, add element to the hash map with its index

#Step 6: Implementation
#Now translate the pseudocode into actual code

def two_sum(nums,target):
  hash_map = {}
  for i, num in enumerate(nums):
    complement = target - num
    if(complement in hash_map):
      return [hash_map[complement], i]
    hash_map[num] = i
  return[]