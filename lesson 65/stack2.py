import math

class stack:

    def __init__(self,n):
        self.size = n
        self.ar = [0]*n
        self.top1 = -1
        self.top2 = self.size
    def push1(self,x):
        if self.top1 > 0:
            self.top1 -= 1
            self.ar[self.top1] = x
        else:
            print("overflow")
    def push2(self,x):
        if self.top2 < self.size-1:
            self.top2 += 1
            self.ar[self.top2] = x
        else:
            print("overflow")
    def pop1(self):
        if self.top1 <= math.floor(self.size/2):
            x = self.ar[self.top1]
            self.top1 += 1
            return x
        else:
            print("underflow")
            exit(1)
    def pop2(self):
        if self.top2 >= math.floor(self.size/2)+1:
            x = self.ar[self.top2]
            self.top2 -= 1
            return x
        else:
            print("underflow")
            exit(1)
    

obj = stack(3)
obj.push1(3)
obj.push2(3)
print(obj.pop1())

