def two_sum(nums, target):
    complements = {}  # Hash table to store numbers and their indices
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in complements:
            return [complements[complement], i]  # Return the indices of the two numbers
        complements[num] = i  # Store the current number and its index in the hash table

    return []  # Return an empty list if no solution is found

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]