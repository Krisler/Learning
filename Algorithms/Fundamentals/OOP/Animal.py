class Animal:
  def speak(self):
    print("Animal sound")

class Dog(Animal): # Dog inherits from Animal
  def speak(self):
    print("Bark")

dog = Dog()
dog.speak()