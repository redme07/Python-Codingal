from abc import ABC ,abstractmethod

class animal(ABC):
    def move(self):
        pass
class dog(animal):
    def move(self):
        print("i can bark")
class lion(animal):
    def move(self):
        print("i can roar")
class snake(animal):
    def move(self):
        print("i can slither")
class fish(animal):
    def move(self):
        print("i live in water")

obj = snake()
obj1 = fish()
obj2 = lion()
obj3 = dog()

obj.move()
obj1.move()
obj2.move()
obj3.move()