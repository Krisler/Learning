class Dog:
  species = "Canis" # Class attribute

  def __init__(self, name, age):
    self.name = name
    self.age = age

print(Dog.species) # Output: Canis