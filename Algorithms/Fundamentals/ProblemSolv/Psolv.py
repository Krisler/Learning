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

nums = [2,7,11,15]
target = 9

print(two_sum(nums,target))


#Step 7: Testing and Debugging
#After implementation, test the code with various inputs to make sure it works correctly.

#Test Cases:

#nums = [2, 7, 11, 15], target = 9 → Output: [0, 1]
#nums = [1, 5, 3, 6], target = 8 → Output: [1, 3]
#Edge case: nums = [1, 1], target = 2 → Output: [0, 1]
#If it fails, debug using print statements or a debugger to track the values of variables at different points in the code.

# Best Practices for Problem Solving
#Understand the Problem: Don’t rush to code. Spend time understanding the problem and its requirements.
#Optimize Gradually: First, solve the problem in the simplest way (even if inefficient). Then optimize.
#Use Pseudocode: Writing a plan or pseudocode helps clarify the solution before coding.
#Test with Edge Cases: Always consider edge cases, such as empty inputs, negative numbers, or large inputs.
#Refactor Code: After solving the problem, refactor to make your code cleaner and more readable.