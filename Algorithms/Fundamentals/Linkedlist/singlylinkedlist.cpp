/*A singly linked list is a data structure that consists
of nodes where each node contains a data element
 and a reference (or pointer) to the next node in the sequence*/
// Dipiction: 5->6->7->8

#include <iostream>

// Node structure representing an element in the linked list
template <typename T>
struct Node
{
    T data;
    Node *next;

    Node(T value) : data(value), next(nullptr) {}
};

// Singly Linked List class
template <typename T>
class SinglyLinkedList
{
private:
    Node<T> *head;

public:
    // Constructor
    SinglyLinkedList() : head(nullptr) {}

    // Insert a new element at the end of the list
    void append(T value)
    {
        Node<T> *newNode = new Node<T>(value);
        if (!head)
        {
            head = newNode;
            return;
        }

        Node<T> *current = head;
        while (current->next)
        {
            current = current->next;
        }
        current->next = newNode;
    }

    // Display the elements in the linked list
    void display()
    {
        Node<T> *current = head;
        while (current)
        {
            std::cout << current->data << " ";
            current = current->next;
        }
        std::cout << std::endl;
    }

    // Destructor to free memory
    ~SinglyLinkedList()
    {
        Node<T> *current = head;
        while (current)
        {
            Node<T> *next = current->next;
            delete current;
            current = next;
        }
    }
};

int main()
{
    SinglyLinkedList<int> myList;

    myList.append(1);
    myList.append(2);
    myList.append(3);

    std::cout << "Linked List Elements: ";
    myList.display();

    return 0;
}
