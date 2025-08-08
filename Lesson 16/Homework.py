confarmation = input("Would you like to shutdown yes or no")

def shut(confarmation):
    if confarmation == "yes" or confarmation == "Yes":
        print("Shutdown")
    elif confarmation == "no" or confarmation == "No":
        print("Abort shut down")
    else:
        print("Sorry")

shut(confarmation)
