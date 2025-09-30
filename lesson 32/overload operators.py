class a:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if self.a<other.a:
            return "a is less than b"
        else:
            return "a is greater than b"
    def __eq__(self,other):
        if self.a == other.a:
            return "a and b are equal"
        else:
            return "a and b are not equal"

ob1 = a(10)
ob2 = a(12)

print(ob1<ob2)
print(ob1==ob2)