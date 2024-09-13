class BankAccount:
  def __init__(self, balance):
    self._balance = balance # Protected attribute
  
  def deposit(self, amount):
    self._balance += amount

  def __secret_method(self):  # Private method
    print("This is secret")

account = BankAccount(100)
account.deposit(50)
print(account._balance)  # Output: 150
# account.__secret_method()  # Raises AttributeError
  
