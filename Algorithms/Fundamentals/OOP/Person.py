class Person:
  def __init__(self, name, age):  #constructor
    self.name = name
    self.age = age
    print(f"{self.name} aquired")

  def __del__(self):    #destructor
    print(f"{self.name} released")

person1 = Person("Alice", 25)
print(person1.name) # Output: Alice
del person1