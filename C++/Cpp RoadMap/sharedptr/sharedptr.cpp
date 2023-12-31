#include <iostream>
#include <memory>

class MyClass {
    public:
        MyClass() { std::cout << "Constructor is called." << std::endl;}
        ~MyClass() { std::cout << "Destructor is called." << std::endl;}
};

int main() {
     // create a shared pointer to manage the MyClass object
    std::shared_ptr<MyClass> ptr1(new MyClass());
    
    {
        // create another shared pointer and initialize it with the previously created pointer
        std::shared_ptr<MyClass> ptr2 = ptr1;

        std::cout << "Inside the inner scope." << std::endl;
        // both pointers share the same object, and the reference counter has been increased to 2
    }

    std::cout << "Outside the inner scope." << std::endl;
    // leaving the inner scope will destroy ptr2, and the reference counter is decremented to 1
    
    // the main function returns, ptr1 goes out of scope, and the reference counter becomes 0
    // this causes the MyClass object to be deleted and the destructor is called
}