class Bird:
  def speak(self):
    print("Chirp")

class Parrot(Bird):
  def speak(self):
    print("Squawk")

parrot = Parrot()
parrot.speak() # Output: Squawk