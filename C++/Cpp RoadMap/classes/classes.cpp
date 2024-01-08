#include <iostream>

class Dog
{
public:
    std::string name;
    int age;

    void bark()
    {
        std::cout << name << " barks!" << std::endl;
    }
};

int main()
{
    Dog myDog;
    myDog.name = "Fido";
    myDog.age = 3;
    myDog.bark(); // Output: Fido barks!
}