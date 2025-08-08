invalid = False

while not invalid:

    try:
        n = int(input("Enter a number"))
        while n%2 == 0:
            print("Bye")
        invalid = True
    except:
        print("Invalid")