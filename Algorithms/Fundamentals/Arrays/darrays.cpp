#include <iostream>
#include <vector>
int main()
{
    // Manual creation
    // Dynamic array creation
    int size;
    std::cout << "Enter the size of the dynamic array: ";

    // Memory allocation
    int *dynamicArray = new int[size];

    // Initializing elements
    for (int i = 0; i < size; ++i)
    {
        dynamicArray[i] = i * 10;
    }

    // Accessing and printing elements
    std::cout << "Dynamic Array Elements: ";
    for (int i = 0; i < size; ++i)
    {
        std::cout << dynamicArray[i] << " ";
    }

    // Memory deallocation
    delete[] dynamicArray;

    // Using an appropriate data structure
    // Dynamic array using std::vector
    int size;
    std::cout << "Enter the size of the dynamic array: ";
    std::cin >> size;

    // Initializing elements
    std::vector<int> dynamicArray(size);
    for (int i = 0; i < size; ++i)
    {
        dynamicArray[i] = i * 10;
    }

    // Accessing and printing elements
    std::cout << "Dynamic Array Elements: ";
    for (int i = 0; i < size; ++i)
    {
        std::cout << dynamicArray[i] << " ";
    }

    // No need for explicit memory deallocation

    return 0;
}