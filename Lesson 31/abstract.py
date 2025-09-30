from abc import ABC, abstractmethod

class abcclass(ABC):
    def print(self, x):
        print("the value of x is", x)
    
    @abstractmethod
    def task(self):
        print("abstract method")

class test_class(abcclass):
    def task(self):
        print("child class")

test = test_class()
test.print(100)
test.task()
