import array

my_array = array.array('i',[10,20, 30]) #Creation of Arrays

# Accessing elements in an array: O(1)
first_element = my_array[0] # Output: 10
print(f"{first_element}\n")

my_array[1] = 25 # Modify the second element
print(my_array)

my_array.append(40) # Adding and element at the end: O(1)
my_array.remove(25) # Removing a specific element: O(n)
print(my_array)

# traversing: O(n)

for item in my_array:
  print(item)