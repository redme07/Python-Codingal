try:# This is done to test a specific block of code
    number = int(input("Enter a number"))
    print("The number you have enetred is", number)

except ValueError as ve: #ValueError is when the wrong data type is enterd in the input
    print("You have entered the wrong data type", ve)