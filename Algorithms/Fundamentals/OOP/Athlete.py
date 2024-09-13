class Swimmer:
    def swim(self):
        print("Swimming")

class Runner:
    def run(self):
        print("Running")

class Triathlete(Swimmer, Runner):
    pass

athlete = Triathlete()
athlete.swim()  # Output: Swimming
athlete.run()   # Output: Running