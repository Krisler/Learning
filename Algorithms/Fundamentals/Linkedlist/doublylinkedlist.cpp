#include <iostream>

// Node structure representing an element in the doubly linked list
template <typename T>
struct Node
{
    T data;
    Node *next;
    Node *prev;

    Node(T value) : data(value), next(nullptr), prev(nullptr) {}
};

// Doubly Linked List class
template <typename T>
class DoublyLinkedList
{
private:
    Node<T> *head;
    Node<T> *tail;

public:
    // Constructor
    DoublyLinkedList() : head(nullptr), tail(nullptr) {}

    // Insert a new element at the end of the list
    void append(T value)
    {
        Node<T> *newNode = new Node<T>(value);
        if (!head)
        {
            head = tail = newNode;
        }
        else
        {
            newNode->prev = tail;
            tail->next = newNode;
            tail = newNode;
        }
    }

    // Display the elements in the linked list forward
    void displayForward()
    {
        Node<T> *current = tail;
        while (current)
        {
            std::cout << current->data << " ";
            current = current->prev;
        }
        std::cout << std::endl;
    }

    // Destructor to free memory
    ~DoublyLinkedList()
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
    // Creating a doubly linked list
    DoublyLinkedList<int> myDoublyList;

    // Adding elements to the list
    myDoublyList.append(1);
    myDoublyList.append(2);
    myDoublyList.append(3);

    // Displaying the list in both directions
    std::cout << "Doubly Linked List (Forward): ";
    myDoublyList.displayForward();

    std::cout << "Doubly Linked List (Backward): ";
    myDoublyList.displayBackward();

    return 0;
}