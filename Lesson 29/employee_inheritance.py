class parent:
    def __init__(self,id,name):
    
        self.id = id
        self.name = name
    
    def display(self):
        print(self.id)
        print(self.name)

class employee(parent):
    def __init__(self,id,name,salary,post):
        self.salary = salary
        self.post = post

        parent.__init__(self,id,name)
    

obj = employee(1234,"Tom",123456,"engineer")
obj.display()
print(obj.salary,"\n",obj.post)