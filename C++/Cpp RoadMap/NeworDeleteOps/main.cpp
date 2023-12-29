#include <iostream>

int main() {
    int* ptr = new int; // Dynamically allocates an int on the heap
    *ptr = 42; // Assigns the value 42 to a;;ocated int
    std::cout<<*ptr<<std::endl;
    delete ptr; // Deallocates the memory assigned to ptr
    //std::cout<<ptr<<std::endl;

    int n = 10;
    int* arr = new int[n]; // Dynamically allocates an array of 10 integers on the heap

    // Set some values in the array
    for (int i = 0; i < n; i++) {
        arr[i] = i;
    }
    std::cout<<arr[1]<<std::endl;
    delete[] arr; // Deallocates the memory assigned to the array
    //std::cout<<arr[1]<<std::endl;
}