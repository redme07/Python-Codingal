class employee:

    def __init_(self):
        print("employee created")

    def __del__(self):
        print("destructor called")

def createobject():
    print("Making object")
    ob1 = employee()
    print("end fuction")
    return ob1

print("calling create_object function")
var = createobject()
print("endprogram")
#destructor always called at end