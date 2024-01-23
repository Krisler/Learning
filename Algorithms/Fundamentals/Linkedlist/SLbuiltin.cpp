#include <iostream>
#include <forward_list>

int main()
{
    // Creating a forward list
    std::forward_list<int> myList;

    // Adding elements to the forward list
    myList.push_front(3);
    myList.push_front(2);
    myList.push_front(1);

    // Displaying the elements in the forward list
    std::cout << "Forward List Elements: ";
    for (const auto &element : myList)
    {
        std::cout << element << " ";
    }
    std::cout << std::endl;

    // Adding an element after the first element
    auto it = myList.begin();
    ++it; // Move to the second element
    myList.insert_after(it, 4);

    // Displaying the modified forward list
    std::cout << "Modified Forward List: ";
    for (const auto &element : myList)
    {
        std::cout << element << " ";
    }
    std::cout << std::endl;

    return 0;
}
