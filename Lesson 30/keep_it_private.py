class A:
    __private_var = 78

    def __private_method(self):
        print("I am in class A")

    def hello(self):
        print(A.__private_var)

obj = A()
obj.hello()
obj.__private_method()
#this cannot be accesed because it is private