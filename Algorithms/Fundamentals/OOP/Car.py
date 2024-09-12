class Car:
  def __init__(self, brand, model):
    self.brand = brand # Instance attribute
    self.model = model
  
  def display_info(self):
    print(f"Car: {self.brand} {self.model}")

# Creating objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.display_info() # Output: Car: Toyota Corolla
car2.display_info()