a = int(input("Enter a number"))
def age(age):
    try:
        if a <= 0:
            raise ValueError("Age cannot be negetive")
        if a%2 == 0:
            print("The age is even")
        else:
            print("The age is odd")

    except ValueError:
        print("Invalid age entered", ValueError)    


age(a)  
            